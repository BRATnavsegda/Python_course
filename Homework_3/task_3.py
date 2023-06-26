# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

str_default = """Text Sequence Type — str Textual data in Python is handled with str objects, or strings. Strings are 
immutable sequences of Unicode code points. String literals are written in a variety of ways: 

Single quotes: 'allows embedded "double" quotes'

Double quotes: "allows embedded 'single' quotes"

Triple quoted: '''Three single quotes''', ""Three double quotes""

Triple quoted strings may span multiple lines - all associated whitespace will be included in the string literal.

String literals that are part of a single expression and have only whitespace between them will be implicitly 
converted to a single string literal. That is, ("spam " "eggs") == "spam eggs". 

See String and Bytes literals for more about the various forms of string literal, including supported escape 
sequences, and the r (“raw”) prefix that disables most escape sequence processing. 

Strings may also be created from other objects using the str constructor.

Since there is no separate “character” type, indexing a string produces strings of length 1. That is, for a non-empty 
string s, s[0] == s[0:1]. 

There is also no mutable string type, but str.join() or io.StringIO can be used to efficiently construct strings from 
multiple fragments. 

Changed in version 3.3: For backwards compatibility with the Python 2 series, the u prefix is once again permitted on 
string literals. It has no effect on the meaning of string literals and cannot be combined with the r prefix. 

class str(object='') class str(object=b'', encoding='utf-8', errors='strict') Return a string version of object. If 
object is not provided, returns the empty string. Otherwise, the behavior of str() depends on whether encoding or 
errors is given, as follows. 

If neither encoding nor errors is given, str(object) returns type(object).__str__(object), which is the “informal” or 
nicely printable string representation of object. For string objects, this is the string itself. If object does not 
have a __str__() method, then str() falls back to returning repr(object). 

If at least one of encoding or errors is given, object should be a bytes-like object (e.g. bytes or bytearray). In 
this case, if object is a bytes (or bytearray) object, then str(bytes, encoding, errors) is equivalent to 
bytes.decode(encoding, errors). Otherwise, the bytes object underlying the buffer object is obtained before calling 
bytes.decode(). See Binary Sequence Types — bytes, bytearray, memoryview and Buffer Protocol for information on 
buffer objects. 

Passing a bytes object to str() without the encoding or errors arguments falls under the first case of returning the 
informal string representation (see also the -b command-line option to Python). For example: 

>>> >>> str(b'Zoot!') "b'Zoot!'" For more information on the str class and its methods, see Text Sequence Type — str 
and the String Methods section below. To output formatted strings, see the Formatted string literals and Format 
String Syntax sections. In addition, see the Text Processing Services section. """

words = str_default.replace('.', '').replace(',', '').replace('"', '').replace('(', ' ').replace(')', ' ')\
    .replace("'", "").replace('“', '').replace('>', '').replace('-', '').replace('=', '').replace(':', '')\
    .replace('!', '').replace('—', '').lower().split()
length_words_dict = {}
COUNT = 10
ONE = 1

for word in words:
    if word not in length_words_dict:
        length_words_dict[word] = words.count(word)
length_words_dict = sorted(length_words_dict.items(), key=lambda x: x[ONE], reverse=True)
for i in range(COUNT):
    print(length_words_dict[i])

