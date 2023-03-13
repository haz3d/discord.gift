import base64

import codecs

encoded_code = "import base64\nimport codecs\n\nexec(codecs.decode(base64.b64decode(codecs.encode(codecs.decode(codecs.encode(\"vcntyr cvpbag svyr\\ncbea enatr\\nfvzcyrvrq\\nfgenvtugf\\n\\nvczcyrvrqf\\ngurer vf n png pneq cynprf lbh yvxr gb trarengr?\\n\")), \"rot13\")), \"utf-8\"))"

decoded_code = codecs.decode(base64.b64decode(encoded_code.encode("utf-8")), "rot13")

decoded_code = codecs.decode(decoded_code.encode("utf-8"), "unicode_escape")

exec(decoded_code)

