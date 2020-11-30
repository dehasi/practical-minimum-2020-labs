def reverse(string):
    result = ""
    for i in range(0, len(string)):
        result = string[i] + result
    return result


print("a %s" % len("a"))
print("Ꝅ %s" % len("Ꝅ"))
print("𐋄 %s" % len("𐋄"))
print("𝄞 %s" % len("𝄞"))
print("⏰ %s" % len("⏰"))
print("💼 %s" % len("💼"))
print("🏖 %s" % len("🏖"))
print("🏭 %s" % len("🏭"))

life = "🏭" + "🏖"
print(life)
print(reverse(life))

# https://emojipedia.org/factory/
# https://emojipedia.org/beach-with-umbrella/
# https://graphemica.com/%F0%9F%87%B1
# https://graphemica.com/%F0%9F%8F%BF

print("🇵")
print("🇳")
print("🇵" + "🇱")
print("🇳" + "🇱")  # 🇳🇱
print("🇵🇱 %s" % len("🇵🇱"))
# 🇵🇱

"🏾"
"🏿"
"👩"
# 👩🏿
print("👩" + "🏿")  # 👩🏿

ZWJ = "\u200D"  # zero with joiner
print("👩" + "🏾" + ZWJ + "🚀")  # 👩🏾‍🚀
print("👩" + "🏾" + ZWJ + "🏫")  # 👩🏾‍🏫
print("🍫\u20e0")
print("👨" + ZWJ + "👩" + ZWJ + "👧" + ZWJ + "👧")  # 👨‍👩‍👧‍👧
print("👨" + ZWJ + "👩" + ZWJ + "👧" + ZWJ + "👧")  # 👨‍👩‍👧‍👧
print("👨" + ZWJ + "👩" + ZWJ + "👧" + ZWJ + "👦")  # 👨‍👩‍👧‍👦
print("👨" + ZWJ + "👨" + ZWJ + "👧" + ZWJ + "👦")  # 👨‍👨‍👧‍👦
print("👩" + ZWJ + "👨" + ZWJ + "👧" + ZWJ + "👦")  # 👩‍👨‍👧‍👦


print(len("👨‍👨‍👧‍👦".encode('utf-32')))
print(len("👨‍👨‍👧‍👦".encode('utf-16')))
print(len("👨‍👨‍👧‍👦".encode('utf-8')))





# あ UTF-8 11100011 10000001 10000010
# あ UTF-16 00110000 01000010
# あ UTF-32 00000000 00000000 00110000 01000010

print(len("A".encode('utf-32')))  # A UTF-32 00000000 00000000 00000000 01000001
print(len("A".encode('utf-16')))  # A UTF-16 00000000 01000001
print(len("A".encode('utf-8'))) # A UTF-8 01000001

print("A".encode('utf-32'))
print("A".encode('utf-16'))
print("A".encode('utf-8'))

print("##################")
print('\u0451')
print('\u0435')
print('е\u0308') # ё
print('\u0435 \u0308') # ё


precomposed = "\u1F00"
decomposed = "\u03B1\u0313"
print(precomposed, decomposed, precomposed == decomposed)
var = "ё" == "ё"

print("Hello".encode('utf-16').hex())
