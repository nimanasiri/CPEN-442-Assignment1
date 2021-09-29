# Answers for All Questions:

## Q1
### a) Plaintext  
OFFWITHTHEIRHEADSANDTHEPROCESSIONMOVEDONCOMMATHREEOFTHESOLDIERSREMAININGBEHINDTOEXECUTETHEUNFORTUNATEGARDENERSCOMMAWHORANTOALICEFORPROTECTIONDOTYOUSHANTBEBEHEADEDSAIDALICECOMMAANDSHEPUTTHEMINTOALARGEFLOWERPOTTHATSTOODNEARDOTTHETHREESOLDIERSWANDEREDABOUTFORAMINUTEORTWOCOMMALOOKINGFORTHEMCOMMAANDTHENQUIETLYMARCHEDOFFAFTERTHEOTHERSDOTARETHEIRHEADSOFFSHOUTEDTHEQUEENDOTTHEIRHEADSAREGONECOMMAIFITPLEASEYOURMAJESTYTHESOLDIERSSHOUTEDINREPLY

### b) Cipher is simple substitution
JOOIEHDHDSECDSKUAKVUHDSZCJTSAAEJVPJYSUJVTJPPKHDCSSJOHDSAJNUESCACSPKEVEVBLSDEVUHJSMSTFHSHDSFVOJCHFVKHSBKCUSVSCATJPPKIDJCKVHJKNETSOJCZCJHSTHEJVUJHGJFADKVHLSLSDSKUSUAKEUKNETSTJPPKKVUADSZFHHDSPEVHJKNKCBSONJISCZJHHDKHAHJJUVSKCUJHHDSHDCSSAJNUESCAIKVUSCSUKLJFHOJCKPEVFHSJCHIJTJPPKNJJXEVBOJCHDSPTJPPKKVUHDSVQFESHNGPKCTDSUJOOKOHSCHDSJHDSCAUJHKCSHDSECDSKUAJOOADJFHSUHDSQFSSVUJHHDSECDSKUAKCSBJVSTJPPKEOEHZNSKASGJFCPKRSAHGHDSAJNUESCAADJFHSUEVCSZNG

### c) Mapping from cipher text (key) to plain text (value)
{'A': 'S', 'B': 'G', 'C': 'R', 'D': 'H', 'E': 'I', 'F': 'U', 'G': 'Y',
'H': 'T', 'I': 'W', 'J': 'O', 'K': 'A', 'L': 'B', 'M': 'X', 
'N': 'L', 'O': 'F', 'P': 'M', 'Q': 'Q', 'R': 'J', 'S': 'E', 'T': 'C', 
'U': 'D', 'V': 'N', 'W': 'Z', 'X': 'K', 'Y': 'V', 'Z': 'P'}

### d)
In q1.py I implemented the hillclimbing algorithm from [here](http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-simple-substitution-cipher/). In my implementation I use the algorithm and data (english_quadgram.txt) taken from [here](http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation) to find the 'fitness' of english text (found in fitness.py). I also spoke with Ningfeng Yang about my algorithm, and had him take a look at my code to check my implementation. Code is contained in q1.py and should less than a minute to complete (sometimes needs to be run a few times).


## Q2
### a) Plaintext
OHCOMMAHEWILLSEEYOUCOMMASAIDTHESOLDIERWHOHADTAKENHERMESSAGETOTHEWIZARDCOMMAALTHOUGHHEDOESNOTLIKETOHAVEPEOPLEASKTOSEEHIMDOTINDEEDCOMMAATFIRSTHEWASANGRYANDSAIDISHOULDSENDYOUBACKWHEREYOUCAMEFROMDOTTHENHEASKEDMEWHATYOULOOKEDLIKECOMMAANDWHENIMENTIONEDYOURSILVERSHOESHEWASVERYMUCHINTERESTEDDOTATLASTITOLDHIMABOUTTHEMARKUPONYOURFOREHEADCOMMAANDHEDECIDEDHEWOULDADMITYOUTOHISPRESENCEDOTIUSTTHENABELLRANGCOMMAANDTHEGREENGIRLSAIDTODOROTHYCOMMATHATISTHESIGNALDOTYOUMUSTGOINTOTHETHRONEROOMALONEDOTSHEOPENEDALITTLEDOORANDDOROTHYWALKEDBOLDLYTHROUGHANDFOUNDHERSELFINAWONDERFULPLACEDOTITWASABIGCOMMAROUNDROOMWITHAHIGHARCHEDROOFCOMMAANDTHEWALLSANDCEILINGANDFLOORWERECOVEREDWITHLARGEEMERALDSSETCLOSELYTOGETHERDOTINTHECENTEROFTHEROOFWASAGREATLIGHTCOMMAASBRIGHTASTHESUNCOMMAWHICHMADETHEEMERALDSSPARKLEINAWONDERFULMANNERDOTBUTWHATINTERESTEDDOROTHYMOSTWASTHEBIGTHRONEOFGREENMARBLETHATSTOODINTHEMIDDLEOFTHEROOMDOTITWASSHAPEDLIKEACHAIRANDSPARKLEDWITHGEMSCOMMAASDIDEVERYTHINGELSEDOTINTHECENTEROFTHECHAIRWASANENORMOUSHEADCOMMAWITHOUTABODYTOSUPPORTITORANYARMSORLEGSWHATEVERDOTTHEREWASNOHAIRUPONTHISHEADCOMMABUTITHADEYESANDANOSEANDMOUTHCOMMAANDWASMUCHBIGGERTHANTHEHEADOFTHEBIGGESTGIANTDOTASDOROTHYGAZEDUPONTHISINWONDERANDFEARCOMMATHEEYESTURNEDSLOWLYANDLOOKEDATHERSHARPLYANDSTEADILYDOTTHENTHEMOUTHMOVEDCOMMAANDDOROTHYHEARDAVOICESAYIAMOZCOMMATHEGREATANDTERRIBLEDOTWHOAREYOUCOMMAANDWHYDOYOUSEEKMEITWASNOTSUCHANAWFULVOICEASSHEHADEXPECTEDTOCOMEFROMTHEBIGHEADSOSHETOOKCOURAGEANDANSWEREDIAMDOROTHYCOMMATHESMALLANDMEEKDOTIHAVECOMETOYOUFORHELPDOTTHEEYESLOOKEDATHERTHOUGHTFULLYFORAFULLMINUTEDOTTHENSAIDTHEVOICEWHEREDIDYOUGETTHESILVERSHOESIGOTTHEMFROMTHEWICKEDWITCHOFTHEEASTCOMMAWHENMYHOUSEFELLONHERANDKILLEDHERCOMMASHEREPLIEDDOTWHEREDIDYOUGETTHEMARKUPONYOURFOREHEADCONTINUEDTHEVOICEDOTTHATISWHERETHEGOODWITCHOFTHENORTHKISSEDMEWHENSHEBADEMEGOODBYEANDSENTMETOYOUCOMMASAIDTHEGIRLDOTAGAINTHEEYESLOOKEDATHERSHARPLYCOMMAANDTHEYSAWSHEWASTELLINGTHETRUTHDOTTHENOZASKEDCOMMAWHATDOYOUWISHMETODOSENDMEBACKTOKANSASCOMMAWHEREMYAUNTEMANDUNCLEHENRYARECOMMASHEANSWEREDEARNESTLYDOTIDONTLIKEYOURCOUNTRYCOMMAALTHOUGHITISSOBEAUTIFULDOTANDIAMSUREAUNTEMWILLBEDREADFULLYWORRIEDOVERMYBEINGAWAYSOLONGDOTTHEEYESWINKEDTHREETIMESCOMMAANDTHENTHEYTURNEDUPTOTHECEILINGANDDOWNTOTHEFLOORANDROLLEDAROUNDSOQUEERLYTHATTHEYSEEMEDTOSEEEVERYPARTOFTHEROOMDOTANDATLASTTHEYLOOKEDATDOROTHYAGAINDOTWHYSHOULDIDOTHISFORYOUASKEDOZDOTBECAUSEYOUARESTRONGANDIAMWEAKBECAUSEYOUAREAGREATWIZARDANDIAMONLYALITTLEGIRLDOTBUTYOUWERESTRONGENOUGHTOKILLTHEWICKEDWITCHOFTHEEASTCOMMASAIDOZ

### b) CIPHER is Playfair:
MKUMGEVPECYNELBLRLDPZOUMGEVPLSDQMILHVRQDRDPNMKYLVYHRSKRDPCNLLSMXGTMIXPKYZLEQTOVPSBMIZOMNECRTLHKGVDNIDMMKSACHRMAELPHIGTHLCEHTRTYDIXRLRXUMGEVPYVQNLKMIXPSLWSOXWPIXLSDQNHKMBRLIXHQIZOVSUHPNRDDPZOBPPCUXTORTGDMIXHECSLHRETXPSPYIZORVZRRXDSHRUMGEVPWSXYECSNPCIGKTHXQIZOLKSDMLLKKMLHECAPLARDPTQUKNIGRDLHMDXLRTVYVDSLYDGTEXKNVPUVQOMICPZLROZMIWZOXUZUCELPEQTOVPWSEIRXCMDQRXECZGBRLYETDYZTQOMKNHZELHXHMCRTYDBKGDMIXHSVREEDWSMFTOVPWSQYECOXRLXHTNDELSDQGTRTUZMIPQTOVPMIYVNHMILHNTSWEXTGZTCOBKGVTKIGTGECMIUZHXUZTOSBGKRXTGHKRMHCHXLYDSGDVDRXGRZUWSXLRTUZMIWASBHRLQVRXEIYKEZOMNWSXQZOIXECLKREQNSWZGIXRDBQEABSMCRTYDGYSLSVNTUMGEVPUZFKXDGRTOYNMIPSNTSPEUECXDGRGUUMGEVPWSQYECAPELBLWSEQDHDSXWWSXQRVZUPXDRUMMLDRXYDYSEZLMXCPRDSBLIHLMQRVHLDAGTMXMIRDRTYDIGECMCIGRDGUMIRDGRGUAPLSOXLPVDNTIMUMGEVPSLULNTIMSLMILHFKUMGEVPPNHQEPYLDMECCPRDSBLIHAZLSRDHSWZGIXRDBQEVWSHXDXTGCQGYSPYDIGRDLHMDXLRTUZMIPTVKGYSLMILCNTMIUZHXGUOXRLXHVPLUERMIYVIVGRTRNSMICPDQXERMQGECUZTORTYDGYSLHKPZRXDSHRPBSPKDWSLIZPURERXYDYNMCPHBTOVPSLQDXRMLDZMINSMXBLRXTGNSMICMXHMDUZQGECMEYSXZSLWSXHZUOTBKECYLUMGEVPYNMIZOVYUVQIGTKBWEZMDODYZUWSWPEOKVDEXMNASPMDMLDXTGMIRDXPSLKGSPKDCZGKMINHECYLUMGEVPCQYDMIYLDPLHWSLYKGHLWSETZOMIUMGEVPWSXYSLOCMEQSWFMXDOSPIGECECYLGUMILCNTMXIVTNWSYQTGSLRTUZMIWTPYRXCZGKMINHNSZGIXRDWSXQLPEUTOVPMIRLDPLHOQXKRXLBGZDAWSXEGRZRRXYVECLKSPEZDAWSLIMDYLSDIQTGMIXHMICPZOMIOTMLEQTOVPWSXLRTUZMIPILPDXSATKMCLSIDPVZKUMGEVPMIXMDRYVWSQYRDDKVBRXTGPNVZDRZTQUTOVPWSXYIPRTZTBKRLRHPCDYAPHSTGKBMEWSPABQBATKMCSLHKCEYLRLHCQMRXGTUMPCUXTOMILCNTECYLKVHKDMGRZRUMOUWVLPIXWSNARDRXSYTEZUTGIPUMGEVPMILHVPELBSIXPCRHRTYDSPMLUMPCGTZTQBZUECEARTGDMIRLDPLHRVZRRXYVECDOKMFOIMBQELDAUGLZBQELEVNSQORXTGMIXHLSDQMILMTKMCPNRDRXDQZTFODMMILHSDMLLKKMLHNTTGMICPUXTOMIXPHQHRXYDYMEGUMIRLLPIVUMGEVPPNXHTPKMBKXCRERVSKRDWSRISDEREIRDUMGEVPHKRDCHDSRXRTGYECDRQDQIZOMXGDMICPZLROZMIWZOXUZUCELPEQGKYDKFRXMILMTKMCRTGDMIYVNHPNRDDMECVTTRYNMQKMQGECKGDOKINHHLETXPECSHECVSXRPCVTTRQALPIXHLIGPCGTZTQUTOVPLSDQMIXMKDEXTGWVYSIGECDPLHRVZRRXYVECLKSPEZDAUMGEVPWSQYECAIPAHKXPSLMDELDSXWMIDMUOMIRTGDMIXHZKSLHREQTOVPPNYVRTZTFZNHEPDMTRVKXHETLCPBIOZRWSLSHBTOVPPNRDCPWPFKMDVPIXFKBECEXHDZZLCMTOVPHKLPSHPXDRXRZLHXIVDARTYDRTIGDSHRZTOUUMFKODPQTOVPSBMIZOMNDYNHKVCLZBYDBQEXTGWSQDPVKBDRZBIGCPYNELBVRXDRYLBQELDAZGDLDKRXTMRDTPCLNSVWAPAIVRGKTXTGMIRLDPLHYNSIRXMIDRDMHTLHUMGEVPWSQYECIGECIYOUHXRQYMTGECMCSDNSVWIXRTNXGTMIXCRVZUWSXDVRERLYUZFKLITUCRRDDAMIYVMIDPHLCPRXGTHLRLLMRDWZZLGTQGECUZTORTVYIXYVBSIVMIDPRVZRRXYVRTUZMIWPVWNSRTGYIPHKZOEXDQTGKNNBZUZTBZHIRXZKRTVQCMZBHLZTBZDRIVUZXWWSQDPVPXZSCLBPBKDPZOZLLPOXLPGYKYZLLYIXSYOTSXWPDSGDVDXMKDEXTGCQYIZOPXDRIVUZXWXHZOMNGTINELDVECYNUHRXYNMQKMQGECLPIVUMGEVPLSDQZK


### c) Key Matrix:
[['Q', 'F', 'B', 'C', 'U'], ['T', 'G', 'V', 'M', 'O'], ['Y', 'W', 'A', 'P', 'Z'], ['I', 'N', 'S', 'H', 'K'], ['D', 'X', 'L', 'E', 'R']]


### d)
I use the simulated annealing algorithm from [here](http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-playfair/). If the algorithm does not find the solution then I shuffle a new key and iterating again. I also had to change the logic to deal with a playfair cipher rather than substitution cipher. While writing it, I checked my algorithm with Ningfeng Yang and also had him take a look at my implementation. He gave me some advice on calculating the fitness scores and adding entropy. Code is contained in q2*.py and should take about 2-5 minutes to produce a correct key, but may need to be re-run a few times. Logs can be found in logfile.txt, and example runs can be found from log3.txt and log4.txt.

## Q3
1.


2. Seconds or ms 


## Q4
1. 

2. Seconds or ms 

