# jp-broom: A Japanese text cleaner

## Description
This project provides a simple text cleaner that removes most of the unecessary characters and symbols in Japanese 
text, while  keeping the original text intact. Japanese texts require different techniques from conventional 
ones, as they tend to include a wide collection of different symbols and emoticons (i.e. kaomoji). 

Original work is from https://github.com/ku-nlp/text-cleaning, but the code has been heavily modified at this point. Primary changes include:
- Conversion from a script-based to a package-based structure
- The package direction moving towards suitability for NLP projects
- Support for more modern versions of Python.

## Cleaning Example

```text
INPUT: これはサンプルです(≧∇≦*)!見てみて→http://a.bc/defGHIjkl
OUTPUT: これはサンプルです！見てみて。

INPUT: 一緒に応援してるよ(o^^o)。ありがとう😃
OUTPUT: 一緒に応援してるよ。ありがとう。

INPUT: いいぞ〜⸜(* ॑꒳ ॑*  )⸝⋆*
OUTPUT: いいぞ。

INPUT: えっ((((；ﾟДﾟ)))))))
OUTPUT: えっ。

INPUT: 確かに「嘘でしょww」って笑ってたね
OUTPUT: 確かに「嘘でしょ。」って笑ってたね。

INPUT: おはようございますヽ(*´∀｀)ノ。。今日は雨ですね･････(T_T)
OUTPUT: おはようございます。今日は雨ですね。

INPUT: (灬º﹃º灬)おいしそうです♡
OUTPUT: おいしそうです。

INPUT: 今日の夜、友達とラーメン行くよ(((o(*ﾟ▽ﾟ*)o)))
OUTPUT: 今日の夜、友達とラーメン行くよ。

# When using the twitter option.
INPUT: @abcde0123 おっとっとwwそうでした✋!！よろしくお願いします♪‼ #挨拶
OUTPUT: おっとっと。そうでした！よろしくお願いします。
```

## Requirements
- Python 3.11+
- mojimoji
- neologdn

## How to Run

1. Import the package `from jp_broom import clean_text`
2. Prepare your text as a string
3. Run `clean_text(text, han2zen= True, twitter=False, repeat = 3)` on your text variable
