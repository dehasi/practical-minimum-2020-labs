Запись в виде графа переходов знанимает достаточно много места. И когда граф растет, читать его становится все труднее.

Но есть и другая форма записи - форме Бэкуса-Наура.
Давайте убедимся, что написание парсера по грамматике - это рутинная операция

### Шаг 0
Напишем грамматику для проверки скобочных выражений в форме Бэкуса-Наура. 
(Это неполный пример, но вы его сможете дополнить, разобравшись как это работает)

```
Exp  -> Term "+" Exp
      | Term

Term -> "(" Exp ")"
      | Int "*" Term
      | Int

Int  -> "1" | "2" | .... | "0"
```

#### Определения
* стартовый символ
* терминальный символ
* нетерминальный символ
* продукция

### Шаг 1
Выстраиваем все в столбик
```
"""
Exp  -> Term "+" Exp
      | Term

Term -> "(" Exp ")"
      | Int "*" Term
      | Int

Int  -> "1" 
      | "2" 
      ....
      | "0"
```
### Шаг 2
Каждая продукция - это функция.
```python
def Exp():  -> Term "+" Exp
      | Term

def Term(): -> "(" Exp ")"
      | Int "*" Term
      | Int

def Int():  -> "1" 
      | "2" 
      ....
      | "0"
```
### Шаг 3
Все нетерминальные символы - это вызов функции.
```python
def Exp():  -> Term() "+" Exp()
      | Term()

def Term(): -> "(" Exp() ")"
      | Int() "*" Term()
      | Int()

def Int():  -> "1" 
      or "2" 
      ....
      or "0"
```
### Шаг 4
Меняем условия "и" и "или" на соответствующие символы в языке программирования, расставляем скобки
```python
def Exp(): 
    (Term() and "+" and Exp()) \
    or Term()

def Term():  
    ("(" and Exp() and ")") \
    or (Int() and "*" and Term())  \
    or Int()

def Int():  
    "1"  \
    or "2"  \
    #....
    or "0"
```

"\\" в конце - это такой способ разделить одну операцию на несколько строк (как в баше)

### Шаг 5
Все терминальные символы парсим через вспомогательную функцию `match`


```python
def match(term):
    return True or False # потом заимплементим

def Exp(): 
    (Term() and match("+") and Exp()) \
    or Term()

def Term():  
    (match("(") and Exp() and match(")")) \
    or (Int() and match("*") and Term())  \
    or Int()

def Int(): 
    match("1")  \
    or match("2")  \
    #....
    or match("0")
```

### Шаг 6
Из-за того что  пример на питоне, заменим `or ...\\` на `if`.
Нам это понадобится в следующем шаге.
```python
def match(term):
    return True or False # потом заимплементим

def Exp(): 
    if Term() and match("+") and Exp(): return True
    if Term(): return True
    return False

def Term():  
    if match("(") and Exp() and match(")"): return True
    if Int() and match("*") and Term() : return True
    if Int(): return True
    return False

def Int(): 
    if match("1"): return True
    if match("2"): return True
    #.....
    if match("0"): return True
    return False
```

### Шаг 7
Входную строку будем обрабатывать символ за символом, добавляем работу с индексами.

```python
NEXT = 0
def match(term):
    return True or False # потом заимплементим

def Exp(): 
    prev = NEXT
    if Term() and match("+") and Exp(): return True
    NEXT = prev
    if Term(): return True
    NEXT = prev
    return False

def Term():  
    prev = NEXT
    if match("(") and Exp() and match(")"): return True
    NEXT = prev
    if Int() and match("*") and Term() : return True
    NEXT = prev
    if Int(): return True
    NEXT = prev
    return False

def Int(): 
    prev = NEXT
    if match("1"): return True
    NEXT = prev
    if match("2"): return True
    #.....
    NEXT = prev
    if match("0"): return True
    NEXT = prev
    return False
```

### Шаг 8
Обернем все в это в клас, заиплементим функцию `match` и убедимся, что все работает.
```python
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
        #....
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
```

Попробуйте построить программы из формы Бэкуса-Наура для 
- чисел с плавающей точкой `123.234E-42`
