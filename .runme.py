try:
    import nicegui
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nicegui'])
import remote_shutter
remote_shutter.main()