import pandas as pd
from pathlib import Path
from md2pdf.core import md2pdf


outdir = 'attendance_certificats'
Path(outdir).mkdir(exist_ok=True)


participants = pd.read_excel('participants_final.xls')
present = participants[participants['Present']==1]

certificat_model = open('attendance_certificat_model.md').read()

for idx, participant in present.iterrows():
    named_certif = certificat_model.replace('{name}', f"{participant['Prénom']} {participant['Nom']}")
    with open(Path(outdir, f"{participant['Nom']}.md"), "w") as file:
        file.write(named_certif)

    md2pdf(Path(outdir, f"{participant['Nom']}.pdf"), md_content=named_certif,
    css_file_path='style.css',base_url='.'
    )
