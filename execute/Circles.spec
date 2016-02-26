# -*- mode: python -*-

block_cipher = None

added_files = [
         ( '../data', 'data' ),
         ( '../images', 'images' ),
         ( '../docx', 'docx' ),
         ]

a = Analysis(['../main.py'],
             pathex=['../', '../utils', '../docx', '/Users/nikolay/Documents/Django_projects/circlesOnTheWater/execute'],
             binaries=None,
             datas=added_files,
             hiddenimports=['docx'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Circles',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='../images/ico.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Circles')
app = BUNDLE(coll,
             name='Circles.app',
             icon='../images/ico.icns',
             bundle_identifier=None)
