# pig.py

## Definition(s)
*pigify* - to translate text into Pig Latin :P

## Synopsis
A command-line Pig Latin translator implemented in Python 3. Can also be used as a module.

## Usage
Command-Line:
```
pig.py [FILE]...
```

Module:
```python
import pig
pig_text = pig.pigify(string)
```

For the command-line, if no files are passed, standard input is used; otherwise, each file that is passed is used. All pigified text is printed to standard output.

## Word Rules
Words are defined by the regex `"[A-z]+([A-z']+[A-z])?"`.
<pre>
Examples:
  "hello"
  "CaMeL"
  "aren't"
  "a'b'c'd"
</pre>

Anything that is not a word is left unpigified.

## Pigification Rules
If the first character of a word is a vowel, "yay" is appended.
<pre>
Examples:
  "Argentina" -> "Argentinayay"
  "Of" -> "Ofyay"
  "isn't" -> "isn'tyay"
</pre>

Otherwise, the first character is brought to the end of the word, and "ay" is appended. For this rule, if the original word is titled, the pigified word is titled.
<pre>
Examples:
  "Python" -> "Ythonpay"
  "dark" -> "arkday"
  "CaMeL" -> "aMeLCay"
</pre>
