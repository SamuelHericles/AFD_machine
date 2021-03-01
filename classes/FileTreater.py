import os

class Treater:
    """
        This class is for just treat txt files.
    """

    def __init__(self,path):
        """
            Constructor class.

            @path - Path where're txt files.

            @return - No return.        
        """
        
        paths = []
        for path, _, files in os.walk(path):
            for afile in files:
                if afile.split('.')[1] == 'txt':
                    paths.append(f"{path}{afile}")

        self.paths = paths

    def treat_input(self, afile):    
        """
            Treat the specific file input to transform in transition function with as matrix.            
            
            @afile - Path of the specific file input.

            @return - The transition function.
        """

        func_transition = []

        afile_treated = afile.split('\n')
        alphabet = afile_treated[0].split(',')
        alphabet = [alphabet[i].split('|')[0].strip() for i in range(0,len(alphabet))]
        func_transition.append(alphabet)

        for step in range(1,len(afile_treated)):
            ftransition = afile_treated[step].split('-')
            transitions = ftransition[1].split(',')
            func_transition.append(transitions)

        return func_transition

    def get_transition_functions(self):
        """
            Treat the all examples in input path.            
            
            @return name_files - The txt files name.
            @return transition_funcs - transitions functions of the folder niput path.
        """

        transition_funcs = []
        name_files = []
        for path in self.paths:
            with open(path,'r') as outfile:
                name_files.append(path.split('/')[1])
                transition_funcs.append(self.treat_input(outfile.read()))
        return name_files, transition_funcs