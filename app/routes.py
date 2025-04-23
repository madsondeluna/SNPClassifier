from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Patient, Variant
from app.utils import consultar_ensembl
from cyvcf2 import VCF
import os

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        file = request.files['vcf_file']
        if name and file:
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)

            patient = Patient(name=name, vcf_filename=file.filename)
            db.session.add(patient)
            db.session.commit()

            vcf = VCF(filename)
            for variant in vcf:
                if len(variant.ALT) == 0: continue
                ann = consultar_ensembl(variant.CHROM, variant.POS, variant.REF, variant.ALT[0])
                v = Variant(
                    patient_id=patient.id,
                    chromosome=variant.CHROM,
                    position=variant.POS,
                    ref=variant.REF,
                    alt=variant.ALT[0],
                    gene=ann.get('gene', ''),
                    consequence=ann.get('consequence', ''),
                    impact=ann.get('impact', ''),
                    sift=ann.get('sift', ''),
                    polyphen=ann.get('polyphen', ''),
                    af=ann.get('af', 0.0),
                    classification=ann.get('classification', 'unknown')
                )
                db.session.add(v)
            db.session.commit()
            return redirect(url_for('index'))

    patients = Patient.query.order_by(Patient.upload_date.desc()).all()
    return render_template('index.html', patients=patients)