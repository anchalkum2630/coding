import tkinter as tk, abc
from typing import List, Tuple, Callable, Iterable, Dict
import inspect


#create formal interface
class IGenericBoard(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        isinterface  = hasattr(subclass, 'read_pin')  and callable(subclass.read_pin)
        isinterface &= hasattr(subclass, 'write_pin') and callable(subclass.write_pin)
        return isinterface

    @abc.abstractmethod
    def generic_pin_read(self, pin:int) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def generic_pin_write(self, pin:int, data:int):
        raise NotImplementedError


#implement IGenericBoard        
class GenericBoard(IGenericBoard):
    @property
    def model(self):
        #the "model type" for this board instance
        return type(self).__name__
        
    @property
    def prefix(self) -> List:
        #the prefix(es) to use when finding functions
        return self._prefix if isinstance(self._prefix , (List, Tuple)) else [self._prefix]
        
    @property
    def msgvar(self) -> tk.StringVar:
        #the output message var
        return self._msgvar
        
    @property
    def attributes(self) -> Dict:
        #get everything in one shot ~ for **kwargs
        return dict(
            model =self.model ,
            prefix=self.prefix,
            msgvar=self.msgvar,
        )

    def __init__(self):
        self._prefix = 'generic'
        self._msgvar = tk.StringVar()

    def generic_pin_read(self, pin:int) -> int:
        self._msgvar.set(f'reading pin {pin}')
        #... really do this
        return 0

    def generic_pin_write(self, pin:int, data:int):
        self._msgvar.set(f'writing {data} on pin {pin}')
        #... really do this


#"final" class
class LEDBoard(GenericBoard):
    def __init__(self):
        GenericBoard.__init__(self)
        self._prefix = self.prefix + ['led']

    def led_blink_write(self, pin:int=13):
        self.generic_pin_write(pin, 1)
        self._msgvar.set(f'blinking on pin {pin}')
        #... really do this


''' tkBaseBoard
        the baseclass for all "tk[Version]Board" classes
        generates form interfaces for methods with the proper prefix(es)
'''
class tkBaseBoard(tk.Frame):
    def __init__(self, master, model, msgvar, prefix, **kwargs):
        tk.Frame.__init__(self, master, **{'bd':2, 'relief':'raised', **kwargs})
        self.grid_columnconfigure(0, weight=1)

        #board model label
        tk.Label(self, text=model, font="Consolas 12 bold").grid(row=0, column=0, sticky='w')

        #message output from board
        self.output_ent = tk.Entry(self, width=30, textvariable=msgvar)
        self.output_ent.grid(row=2, column=0, sticky='e')

        #common feature label configuration
        self.lbl_opts = dict(width=6, anchor='w', font='Consolas 10')
        
        #annotation conversion
        self.conversion = {
            "<class 'int'>"  :lambda: tk.IntVar(),
            "<class 'str'>"  :lambda: tk.StringVar(),
            "<class 'bool'>" :lambda: tk.BooleanVar(),
            "<class 'float'>":lambda: tk.DoubleVar(),
        }

        #build a feature for every "feat_" suffixed method
        for feature in [func for func in dir(self) if callable(getattr(self, func)) and func.split('_')[0] in prefix]:
            self._add_feature(feature)

    #create a list of variable values
    def __tovalue(self, vars) -> List[int]:
        return [v.get() for v in vars]
        
    #dynamically create the gui for a method
    def _add_feature(self, feature):
        main = tk.Frame(self)
        main.grid(sticky='we')
        
        #parse feature components
        command = getattr(self, feature)
        featcmp = feature.split('_')
        
        if featcmp and len(featcmp) == 3:
            _, label, action = featcmp
            
            #create a list of Vars based on command argument types
            args, vars = inspect.signature(command).parameters, []
            for name in args:
                try:
                    #convert annotations to the proper tk.[Type]Var
                    vars.append(self.conversion[str(args[name].annotation)]())
                except KeyError:
                    #fallback to StringVar
                    vars.append(tk.StringVar())
    
            #create label and button for this command
            tk.Label(main, text=label, **self.lbl_opts).grid(row=0, column=0, sticky='e')
            tk.Button(main, text=action, width=5, command=lambda v=vars: command(*self.__tovalue(v))).grid(row=0, column=1, sticky='w', padx=8)
    
            #create an Entry for every argument in command
            for i, v in enumerate(vars):
                tk.Entry(main, width=2, textvariable=v).grid(row=0, column=i+2, sticky='w')
    
            #give all the weight to the last row
            main.grid_columnconfigure(i+2, weight=1)
        else:
            #feature name components did not pass expectations
            raise ValueError('ValueError: feature component must consist of three underscore-seperated parts as: PREFIX_LABEL_ACTION')


##EXAMPLES OF THE ULTIMATE IMPLEMENTATION ALL OF THE ABOVE ALLOWS


#generate GenericBoard display
class tkGenericBoard(tkBaseBoard, GenericBoard):
    def __init__(self, master, **kwargs):
        GenericBoard.__init__(self)
        tkBaseBoard.__init__(self, master, **self.attributes, **kwargs)


#generate LEDBoard display
class tkLEDBoard(tkBaseBoard, LEDBoard):
    def __init__(self, master, **kwargs):
        LEDBoard.__init__(self)
        tkBaseBoard.__init__(self, master, **self.attributes, **kwargs)


##EXAMPLE BASE USAGE


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Example')
    root.configure(padx=2, pady=2)
    
    tkGenericBoard(root).grid()
    
    tkLEDBoard(root).grid()
    
    root.mainloop()