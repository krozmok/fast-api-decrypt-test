def decrypt(freqlang, text):
    try:
        text_length = len(text)
        frequency = {}
        for i in range(text_length):  
            character = text[i].upper()
            if character.isalpha():
                if (frequency.get(character, False)):
                    frequency[character] += 1
                else:
                    frequency[character] = 1
                
        sorted_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

        dict_character_matches = {}
        i = 0
        for char in sorted_frequency.keys():
            dict_character_matches[char] = freqlang[i]
            i += 1
        #print(dict_character_matches)
        decrypted = ""
        for i in range(text_length):
            character = text[i].upper()
            if character.isalpha():
                character = dict_character_matches[character]
            decrypted+=character.lower()
        #print(decyrpted)
        return decrypted
    except Exception as e:
        if len(freqlang) < len(frequency.items()):
            return "El valor de freqlang no es lo suficientemente largo para desencriptar el texto."
        return str(e)
    

if __name__ == "__main__":
    freqlang = "TEOIARNSHLMYUCWDGPFBVKJ"
    text = """uid nx, aex jcdjipx iu wzux zp, ta wxtpa jtdaws, ai etkx vis.
    dcos zyexdzaxr aex jxdw jezwipijes iu etkzyg nidx aety iyx hts
    ai ri aex ptnx aezyg. z zyexdzaxr aeta jezwipijes udin wtdds htww,
    hei zp ns exdi tqactwws. z htya ai ntfx dcos cpxdp udxx. z htya ai
    gzkx aexn aex udxxrin ai qeiipx. jxijwx tdx rzuuxdxya. jxijwx qeiipx
    rzuuxdxya qdzaxdzt. oca zu aexdx zp t oxaaxd hts tniyg ntys
    twaxdytazkxp, z htya ai xyqicdtgx aeta hts os ntfzyg za qinuidatowx.
    pi aeta'p heta z'kx adzxr ai ri.
    z htya ai piwkx jdiowxnp z nxxa zy aex rtzws wzux os cpzyg qinjcaxdp,
    pi z yxxr ai hdzax jdigdtnp. os cpzyg dcos, z htya ai qiyqxyadtax aex
    aezygp z ri, yia aex ntgzqtw dcwxp iu aex wtygctgx, wzfx patdazyg hzae
    jcowzq kizr  pinxaezyg pinxaezyg pinxaezyg ai pts, "jdzya exwwi hidwr."
    z vcpa htya ai pts, "jdzya aezp!" z riy'a htya tww aex pcddicyrzyg
    ntgzq fxshidrp. z vcpa htya ai qiyqxyadtax iy aex atpf. aeta'p aex otpzq
    zrxt. pi z etkx adzxr ai ntfx dcos qirx qiyqzpx tyr pcqqzyqa.
    scfzezdi ntapcniai. (hhh.tdaznt.qin/zyak/dcos)"""
    print(decrypt(freqlang, text))