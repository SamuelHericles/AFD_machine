from datetime import datetime

from .FileTreater import Treater

class AFD:
    """
        This class is for just deterministic finite automaton(DFA) processor.
    """
    def __init__(self, path_ft, q0, qfs, words):
        """
            Class constructor.

            @path_ft - Path where exist automaton examples in txt files.
            @q0      - Initial state.
            @qfs     - Final state(s).
            @word    - Test word(s).

            @return - No return.
        """

        self.treat = Treater(path_ft)

        self.q0 = q0 
        self.qfs = qfs
        self.words = words
        self.process_example()


    def process_example(self):
        """
                This function is for receive parameters q0, qfs and
            word for test in automaton examples folder.

            @return - No return.
        """

        name_files, transition_funcs = self.treat.get_transition_functions()
        for name_file, transition_func in zip(name_files, transition_funcs):
            print(f"Name file: {name_file}")
            self.afd(transition_func, self.q0, self.qfs, self.words)
            print('-'*50)

    def afd(self, transition_func, q0, qfs, word):
        """
                This function is for receive parameters functino transistion, q0, qfs and 
            word and process the automaton deterministic.

            @transition_func - Trasition function.
            @q0              - Initial state.
            @qfs             - Final state(s).
            @word            - Test word.


            @return - If accepter it's mean that the word passed in the 
                      automaton, otherwise don't passed in the automaton.
        """
        
        print(f"{datetime.now()}\n\n::Start processing::\n ",end='')
        print(f"Word: {word}")
        
        if set(list(word)) == set(transition_func[0]):

            Eo = self.q0
            print(f"\n\t{Eo}->",end='')
            for alfa in list(word):
                Eo = transition_func[int(Eo.split("q")[1])+1][transition_func[0].index(alfa)]
                print(f"{Eo}->",end='')

                if(Eo == 'vazio'):
                    return print('end\n\n::End process::\n\t  REJECTED!!!\n')

            if Eo in qfs:
                return print('end\n\n::End process::\n\t  ACCEPTED!!!\n')
                
            else:
                return print('end\n\n::End process::\n\t  REJECTED!!!\n')
                
        else:
            print("\n>>No match, exist symbols that don't include in alphabet!\n")




        

