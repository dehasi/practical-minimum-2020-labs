"""
Exp  -> Term "+" Exp
      | Term
Term -> "(" Exp ")"
      | Int "*" Term
      | Int
Int  -> "1" | "2" | "3" | "4" | .... | "0"
"""

"""
Exp  -> Term "+" Exp
      | Term
Term -> "(" Exp ")"
      | Int "*" Term
      | Int
Int  -> "1" 
      | "2" 
      | "3" 
      | "4" 
      | "5"
      | "6" 
      | "7" 
      | "8" 
      | "9"
      | "0"
"""


class Parser:
    NEXT = 0
    input = ""

    def parse(self, input):
        self.input = input
        self.NEXT = 0
        return self.Exp() and self.whole_parsed()

    def whole_parsed(self):
        return self.NEXT == len(self.input)

    def match(self, term):
        if (self.NEXT < len(self.input)) and (term == self.input[self.NEXT]):
            self.NEXT += 1
            return True
        return False

    def Exp(self):
        prev = self.NEXT
        if self.Term() and self.match("+") and self.Exp(): return True

        self.NEXT = prev
        if self.Term(): return True

        self.NEXT = prev
        return False

    def Term(self):
        prev = self.NEXT
        if self.match("(") and self.Exp() and self.match(")"): return True

        self.NEXT = prev
        if self.Int() and self.match("*") and self.Term(): return True

        self.NEXT = prev
        if self.Int(): return True

        self.NEXT = prev
        return False

    def Int(self):
        prev = self.NEXT
        if self.match("1"): return True
        self.NEXT = prev
        if self.match("2"): return True
        self.NEXT = prev
        if self.match("3"): return True
        self.NEXT = prev
        if self.match("4"): return True
        self.NEXT = prev
        if self.match("5"): return True
        self.NEXT = prev
        if self.match("6"): return True
        self.NEXT = prev
        if self.match("7"): return True
        self.NEXT = prev
        if self.match("8"): return True
        self.NEXT = prev
        if self.match("9"): return True
        self.NEXT = prev
        if self.match("0"): return True

        self.NEXT = prev
        return False


assert not Parser().parse("1+")
assert not Parser().parse("+1")
assert not Parser().parse("+(1")
assert not Parser().parse("+(1)")
assert Parser().parse("1")
assert Parser().parse("1+1")
assert Parser().parse("(1+1)+(2+2)")
assert Parser().parse("1+3*(8+5)")
print("LOL! It works!")
