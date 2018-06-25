import wingapi
import os


_APP = wingapi.gApplication
_PROJECT = _APP.GetProject()

APP = wingapi.gApplication
PROJECT = APP.GetProject()
PROJECT_PATH = str(PROJECT.GetFilename())
PROJECT_NAME = PROJECT_PATH.split('/')[-1]
VENV_PATH = os.path.join(PROJECT_PATH.replace(PROJECT_NAME, ''), 'venv')


def new_virtualenv(python_version):
    try:
        versions = {'3': 'python3', '2': 'python2'}
                
        command = 'virtualenv {0} -p {1}'.format(VENV_PATH, versions[python_version])
        os.system(command)

        # check is running in windows and set correct executable path.
        if os.name == 'nt':
            PROJECT.SetPythonExecutable(filename=None ,executable=os.path.join(VENV_PATH, 'Scripts', 'python'))
        else:
            PROJECT.SetPythonExecutable(filename=None ,executable=os.path.join(VENV_PATH, 'bin', 'python'))

        APP.ShowMessageDialog("New Virtualenv","A new virtualenv created on: \n" + VENV_PATH)
    except Exception as ex:
        APP.ShowMessageDialog("New Virtualenv","Error:\n" + str(ex))


def install_requirements():
    try:
        # check is running in windows and set correct executable path.
        pip_path = ''
        if os.name == 'nt':
            pip_path = os.path.join(VENV_PATH,'bin','pip')
        else:
            pip_path = os.path.join(VENV_PATH,'Scripts','pip')

        requirements_path = os.path.join(PROJECT_PATH.replace(PROJECT_NAME,''),'requirements.txt')
        command = '{} install -r {}'.format(pip_path,requirements_path)
        os.system(command)
        APP.ShowMessageDialog('Install Requiments','Application dependecies installed successfully.\n'+command)
    except Exception as ex:
        APP.ShowMessageDialog('Install Requiments','Error: \n'+str(ex))