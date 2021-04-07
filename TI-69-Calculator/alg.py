#!/usr/bin/env python
import numpy as np
import json
import numbers

# use -, \ for vim panel splits (like tmux) (space+\, since leader=<space>) space+x for closing, etc.

# edit kate gruvbox color scheme, because highlight color for inside (brackets) while in normal mode is swapped and it is silly

# switch for x \times 10^y output, default=True
def sci(base, decimals=3):
    return ("{:." + str(decimals) + "e}").format(base)

# Functions
sqrt = np.sqrt
# TODO: define a sigma function that accepts values for n, i, and expression as a Function object, in function object define adding two functions together as both returning floats and returning strings (add a switch and/or try: ... except: ...) <- Add a switch in sigma function. Also write a cumulative product function Pi that does the same thing for multiplication

# sigma function would have support for x_i notation in the function, would accept lists for each (check against function/multivarfunction using a dictionary

# sigma function could be incorperated as a Function derived class maybe? self.i = 1, self.n = ... (figure out n=inf?? by relearning calculus 2 and incorperating limits or something)

# https://stackoverflow.com/questions/11830261/coding-sigma-formula

# have regex replacer for | ... | -> np.abs( ... )   (if numbers.Real: ... elif type == vector: determinant
# look at linalg definition of abs()
# TODO:
# TODO: Determinants using sigma function!!! would be pretty wacky if I can figure it out
# TODO:
# <..,..> -> np.dot(..,..) (vector functions)
# same for cross product, determinant |v| if we want to expand on linalg skills

#sigma uses np.linspace()?


# TODO: define sigmoid function S(x), would use np.exp(), and have it create a matplotlib plot or something idk

# Constants
e = np.e
pi = np.pi
g = 9.81
G = 6.67e-11

# Symbols
symbols = {
    "\Delta": "∆",
    "\omega": "ω",
    "\mu": "μ"
}


# https://stackoverflow.com/questions/42706665/ask-for-help-for-a-sum-sigma-function

# figure out np.asarray(), np.asanyarray() np.linspace(), np.array([],float)
#for r in x:
#y1.append(np.exp(np.sum((1-r)**2*a*((2*b[:,0]+1)*r-1+r)*(r-1+r)**(b[:,0]-1)))) 

# https://stackoverflow.com/questions/60426653/how-do-you-recreate-sigma-notation-using-numpy
# def composite
# def parser f(x) = ... -> x, ..., y, f
# sum, seq, ...

class Function:
    def __init__(self, argument="", relation="", value="", name="f", is_mutable=False):
        if isinstance(argument, str): self.argument = argument
        else: raise TypeError

        if isinstance(relation, str): self.relation = relation
        else: raise TypeError

        if isinstance(value, str): self.value = value
        else: raise TypeError

        if isinstance(name, str): self.name = name
        else: raise TypeError

        # If Fuction is mutable, variable names can be changed automatically during operations
        if isinstance(is_mutable, bool): self.is_mutable = False
        else: raise TypeError

        self.format_evaluatable(inplace=True)

    def format_evaluatable(self, inplace=False):
        member_dict = self.__dict__
        for member, value in member_dict.items():
            if member not in ["is_mutable"]:
                value = re.sub(r"(.)\(", r"\1*(", value)
                value = re.sub(r"\^", r"\*\*", value)
                for escape_seq, symbol in symbols.items():
                    if escape_seq in value:
                        value = value.replace(escape_seq, symbol)
                    # if "\\frac" in value:
                        # convert \frac{*}{*} to (*)/(*)
                        # r"\\frac\{(.+?)(?=\}\{)\}\{(.+?)(?=\})\}"
                        # captures \frac{.. \x{ } ..}{...} correctly
                        # doesn't capture \frac{...}{.. \x{ } ..} correctly, stops before last '}'
                        # regex is hardddd
                if not inplace:
                    member_dict[member] = value
                else:
                    self.__dict__[member] = value

        if not inplace:
            return member_dict


    def format_readable(self, inplace=False):
        member_dict = self.__dict__
        for member, value in member_dict.items()
            if member not in ["is_mutable"]:
                value = re.sub(r"(.)\*\(", r"\1(", value)
                value = re.sub(r"\*\*", r"\^", value)
                for escape_seq, symbol in symbols.items():
                    if escape_seq in value:
                        value = value.replace(escape_seq, symbol)
                if not inplace:
                    member_dict[member] = value
                else:
                    self.__dict__[member] = value

        if not inplace:
            return member_dict

    def string(self, notation="v"):
        if notation == "v" or notation == "value":
            return f"{self.value} = {self.relation}"
        elif notation == "n" or notation == "name":
            return f"{self.name}({self.argument}) = {self.relation}"

    def __str__(self):
        return self.string()

    def __add__(self, other) -> Function:
        f = self.copy()
        if isinstance(other, Function):
            f.relation = f.relation + " + " + other.relation
            if other.is_mutable:
                f.change_args(f.argument, other.argument)
        elif isinstance(other, str) or isinstance(other, int) or isinstance(other, float):
            s.relation = s.relation + " + " + str(other)
        else:
            raise TypeError
        return s

    def __radd__(self, other) -> Function:
        return self + other

    def __iadd__(self, other) -> Function:
        if isinstance(other, Function):
            self.relation = self.relation + " + " + other.relation
            if other.is_mutable:
                self.change_args(self.argument, other.argument)
        elif isinstance(other, str) or isinstance(other, int) or isinstance(other, float):
            self.relation = self.relation + " + " + str(other)
        else:
            raise TypeError
        return self

    def json(self):
        return json.dumps(self.format_readable())

    def copy(self) -> Function:
        return Function(self.argument, self.relation, self.value, self.name, self.is_mutable)

    def equals(self, other: Function):
        if isinstance(other, Function):
            for key, value in other.__dict__.items():
                self.__dict__[key] = value
        else: raise TypeError

    def change_args(self, new: str, old=None):
        if self.is_mutable and isinstance(new, str):
            if old is not None:
                if isinstance(old, str):
                    self.relation = re.sub(old, new, self.relation)
                elif isinstance(old_arg, list):
                    for s in old:
                        self.relation = re.sub(s, new, self.relation)
                else: raise TypeError

            self.relation = re.sub(self.argument, new, self.relation)
            self.argument = new

    def of(self, other, return_string=False):
        f = self.copy()
        if isinstance(other, numbers.Real) or isinstance(other, str):
            f.relation = re.sub(f.argument, f"({other})", f.relation)
            f.format_evaluatable(inplace=True)
            try:
                if not isinstance(other, str):
                    result = eval(f.relation)
                    if return_string: return str(result)
                    else: return result

            if return_string: return f.relation
            else:
                return f

        elif isinstance(other, Function):
            f.relation = re.sub(f.argument, f"({other.relation})", f.relation)
            if return_string: return f.relation
            else:
                f.change_args(other.argument)
                return f

        elif isinstance(other, list):
            return [self.of(x) for x in other]

        else:
            raise TypeError

class MultivarFunction(Function):
    def __init__(self, expression=None, variables="", name="f"):
        if isinstance(expression, str):
            self.expression = expr.replace(")(",")*(").replace("^","**")
            self.variables = variables
            if not isinstance(self.variables, list):
                raise TypeError
            self.name = name
        else:
            raise TypeError
    def __str__(self):
        if "=" not in self.expresion:
            variables = str(self.variables)
            for v in ["'","[","]"]:
                variables = variables.replace(v,"")
            return f"{self.name}({self.variables}) = {self.expression}"
        else: return self.expression


def main():
    pass

if __name__ == "__main__":
    main()
