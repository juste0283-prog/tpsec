#!/usr/bin/env python3
# Vérification de prudence pour le dépôt (les faux positifs sont possibles).
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parents[1]
patterns=[r'(?i)secret\s*=\s*["\']?[^\s"\']+',r'(?i)Cleartext-Password\s*:=\s*["\'][^"\']+',r'-----BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY-----']
issues=[]
for p in root.rglob('*'):
 if not p.is_file() or '.git' in p.parts or p.suffix.lower() in ('.png','.jpg','.pdf','.docx','.zip'):continue
 try:s=p.read_text(encoding='utf-8')
 except:continue
 if p.suffix=='.example':continue # Exemples contiennent uniquement des placeholders
 for patt in patterns:
  if re.search(patt,s):issues.append(str(p.relative_to(root)))
print('Fichiers a examiner :', sorted(set(issues)))
sys.exit(bool(issues))
