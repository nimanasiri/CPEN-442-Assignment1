import q2_helpers
import sys
import math
import fitness
import random
import numpy as np
import logging
from datetime import datetime

random.seed(datetime.now())

ciphertext = "MKUMGEVPECYNELBLRLDPZOUMGEVPLSDQMILHVRQDRDPNMKYLVYHRSKRDPCNLLSMXGTMIXPKYZLEQTOVPSBMIZOMNECRTLHKGVDNIDMMKSACHRMAELPHIGTHLCEHTRTYDIXRLRXUMGEVPYVQNLKMIXPSLWSOXWPIXLSDQNHKMBRLIXHQIZOVSUHPNRDDPZOBPPCUXTORTGDMIXHECSLHRETXPSPYIZORVZRRXDSHRUMGEVPWSXYECSNPCIGKTHXQIZOLKSDMLLKKMLHECAPLARDPTQUKNIGRDLHMDXLRTVYVDSLYDGTEXKNVPUVQOMICPZLROZMIWZOXUZUCELPEQTOVPWSEIRXCMDQRXECZGBRLYETDYZTQOMKNHZELHXHMCRTYDBKGDMIXHSVREEDWSMFTOVPWSQYECOXRLXHTNDELSDQGTRTUZMIPQTOVPMIYVNHMILHNTSWEXTGZTCOBKGVTKIGTGECMIUZHXUZTOSBGKRXTGHKRMHCHXLYDSGDVDRXGRZUWSXLRTUZMIWASBHRLQVRXEIYKEZOMNWSXQZOIXECLKREQNSWZGIXRDBQEABSMCRTYDGYSLSVNTUMGEVPUZFKXDGRTOYNMIPSNTSPEUECXDGRGUUMGEVPWSQYECAPELBLWSEQDHDSXWWSXQRVZUPXDRUMMLDRXYDYSEZLMXCPRDSBLIHLMQRVHLDAGTMXMIRDRTYDIGECMCIGRDGUMIRDGRGUAPLSOXLPVDNTIMUMGEVPSLULNTIMSLMILHFKUMGEVPPNHQEPYLDMECCPRDSBLIHAZLSRDHSWZGIXRDBQEVWSHXDXTGCQGYSPYDIGRDLHMDXLRTUZMIPTVKGYSLMILCNTMIUZHXGUOXRLXHVPLUERMIYVIVGRTRNSMICPDQXERMQGECUZTORTYDGYSLHKPZRXDSHRPBSPKDWSLIZPURERXYDYNMCPHBTOVPSLQDXRMLDZMINSMXBLRXTGNSMICMXHMDUZQGECMEYSXZSLWSXHZUOTBKECYLUMGEVPYNMIZOVYUVQIGTKBWEZMDODYZUWSWPEOKVDEXMNASPMDMLDXTGMIRDXPSLKGSPKDCZGKMINHECYLUMGEVPCQYDMIYLDPLHWSLYKGHLWSETZOMIUMGEVPWSXYSLOCMEQSWFMXDOSPIGECECYLGUMILCNTMXIVTNWSYQTGSLRTUZMIWTPYRXCZGKMINHNSZGIXRDWSXQLPEUTOVPMIRLDPLHOQXKRXLBGZDAWSXEGRZRRXYVECLKSPEZDAWSLIMDYLSDIQTGMIXHMICPZOMIOTMLEQTOVPWSXLRTUZMIPILPDXSATKMCLSIDPVZKUMGEVPMIXMDRYVWSQYRDDKVBRXTGPNVZDRZTQUTOVPWSXYIPRTZTBKRLRHPCDYAPHSTGKBMEWSPABQBATKMCSLHKCEYLRLHCQMRXGTUMPCUXTOMILCNTECYLKVHKDMGRZRUMOUWVLPIXWSNARDRXSYTEZUTGIPUMGEVPMILHVPELBSIXPCRHRTYDSPMLUMPCGTZTQBZUECEARTGDMIRLDPLHRVZRRXYVECDOKMFOIMBQELDAUGLZBQELEVNSQORXTGMIXHLSDQMILMTKMCPNRDRXDQZTFODMMILHSDMLLKKMLHNTTGMICPUXTOMIXPHQHRXYDYMEGUMIRLLPIVUMGEVPPNXHTPKMBKXCRERVSKRDWSRISDEREIRDUMGEVPHKRDCHDSRXRTGYECDRQDQIZOMXGDMICPZLROZMIWZOXUZUCELPEQGKYDKFRXMILMTKMCRTGDMIYVNHPNRDDMECVTTRYNMQKMQGECKGDOKINHHLETXPECSHECVSXRPCVTTRQALPIXHLIGPCGTZTQUTOVPLSDQMIXMKDEXTGWVYSIGECDPLHRVZRRXYVECLKSPEZDAUMGEVPWSQYECAIPAHKXPSLMDELDSXWMIDMUOMIRTGDMIXHZKSLHREQTOVPPNYVRTZTFZNHEPDMTRVKXHETLCPBIOZRWSLSHBTOVPPNRDCPWPFKMDVPIXFKBECEXHDZZLCMTOVPHKLPSHPXDRXRZLHXIVDARTYDRTIGDSHRZTOUUMFKODPQTOVPSBMIZOMNDYNHKVCLZBYDBQEXTGWSQDPVKBDRZBIGCPYNELBVRXDRYLBQELDAZGDLDKRXTMRDTPCLNSVWAPAIVRGKTXTGMIRLDPLHYNSIRXMIDRDMHTLHUMGEVPWSQYECIGECIYOUHXRQYMTGECMCSDNSVWIXRTNXGTMIXCRVZUWSXDVRERLYUZFKLITUCRRDDAMIYVMIDPHLCPRXGTHLRLLMRDWZZLGTQGECUZTORTVYIXYVBSIVMIDPRVZRRXYVRTUZMIWPVWNSRTGYIPHKZOEXDQTGKNNBZUZTBZHIRXZKRTVQCMZBHLZTBZDRIVUZXWWSQDPVPXZSCLBPBKDPZOZLLPOXLPGYKYZLLYIXSYOTSXWPDSGDVDXMKDEXTGCQYIZOPXDRIVUZXWXHZOMNGTINELDVECYNUHRXYNMQKMQGECLPIVUMGEVPLSDQZK"

#key = [['U','Q','F','B','C'],['O','T','G','V','M'],['Z','Y','W','A','P'],['K','I','N','S','H'],['R','D','X','L','E']]
#key = [['T','G','V','M','O'],['Y','W','A','P','Z'],['I','N','S','H','K'],['D','X','L','E','R'],['Q','F','B','C','U']]
key = [['N', 'Q', 'W', 'E', 'F'], ['O', 'P', 'S', 'D', 'A'], ['M', 'K', 'B', 'Z', 'X'], ['I', 'T', 'U', 'H', 'R'], ['G', 'C', 'Y', 'L', 'V']]


pt = ''.join(q2_helpers.decode(key, ciphertext))

print(pt)
print(q2_helpers.fitness(pt))
print(fitness.total_fitness(pt))

max_key = list(key)