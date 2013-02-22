import setuptools
import virtualenv


class RunTests(setuptools.Command):

    user_options = []

    def initialize_options(self,):
        pass

    def finalize_options(self,):
        pass

    def run(self,):
        virtualenv.create_environment('./tmp', use_distribute=True)