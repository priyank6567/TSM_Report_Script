# -*- mode: python -*-
a = Analysis(['..\\genReport.py'],
             pathex=['C:\\Users\\Pranky\\AppData\\Backup\\Pranky\\PrankyProjects\\Python_Scripting\\Scripts\\Visteon_Automation\\EXE'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='genReport.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
