from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import tkinter.messagebox
import time
import sys
import os

# this defined function is supposed to allow you to add files to the executable without having them in the root directory, idk how/if it works
# shoutout to Rainer Neimann on stackoverflow for giving an explanation for how to do this!
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



############################################################## --- beginning of interface setup + displaying logo



root = Tk()
root.configure(bg="#FFFFFF")
root.title("Arpasing OTO Reorderer Tool Application")
root.geometry("600x240+0+0")
root.resizable(False, False)

# creates an image object
logoImg = ImageTk.PhotoImage(Image.open(resource_path("logo_6-22-23.png")))

# creates a new label for the image
logo_lbl = ttk.Label(root, image=logoImg)
logo_lbl.place(x=0, y=0)



############################################################### --- defining some variables and functions



V_TUPLE = ("aa", "ae", "ah", "ao", "ax", "eh", "er", "ih", "iy", "uh", "uw", "aw", "ay", "ey", "ow", "oy", "-")
C_TUPLE = ("b", "ch", "d", "dh", "dx", "f", "g", "hh", "jh", "k", "l", "m", "n", "ng", "p", "q", "r", "s", "sh", "t", "th", "v", "w", "y", "z", "zh")
VV_TUPLE = ('aa aa', 'aa ae', 'aa ah', 'aa ao', 'aa ax', 'aa eh', 'aa er', 'aa ih', 'aa iy', 'aa uh', 'aa uw', 'aa aw', 'aa ay', 'aa ey', 'aa ow', 'aa oy', 'aa -', 'ae aa', 'ae ae', 'ae ah', 'ae ao', 'ae ax', 'ae eh', 'ae er', 'ae ih', 'ae iy', 'ae uh', 'ae uw', 'ae aw', 'ae ay', 'ae ey', 'ae ow', 'ae oy', 'ae -', 'ah aa', 'ah ae', 'ah ah', 'ah ao', 'ah ax', 'ah eh', 'ah er', 'ah ih', 'ah iy', 'ah uh', 'ah uw', 'ah aw', 'ah ay', 'ah ey', 'ah ow', 'ah oy', 'ah -', 'ao aa', 'ao ae', 'ao ah', 'ao ao', 'ao ax', 'ao eh', 'ao er', 'ao ih', 'ao iy', 'ao uh', 'ao uw', 'ao aw', 'ao ay', 'ao ey', 'ao ow', 'ao oy', 'ao -', 'ax aa', 'ax ae', 'ax ah', 'ax ao', 'ax ax', 'ax eh', 'ax er', 'ax ih', 'ax iy', 'ax uh', 'ax uw', 'ax aw', 'ax ay', 'ax ey', 'ax ow', 'ax oy', 'ax -', 'eh aa', 'eh ae', 'eh ah', 'eh ao', 'eh ax', 'eh eh', 'eh er', 'eh ih', 'eh iy', 'eh uh', 'eh uw', 'eh aw', 'eh ay', 'eh ey', 'eh ow', 'eh oy', 'eh -', 'er aa', 'er ae', 'er ah', 'er ao', 'er ax', 'er eh', 'er er', 'er ih', 'er iy', 'er uh', 'er uw', 'er aw', 'er ay', 'er ey', 'er ow', 'er oy', 'er -', 'ih aa', 'ih ae', 'ih ah', 'ih ao', 'ih ax', 'ih eh', 'ih er', 'ih ih', 'ih iy', 'ih uh', 'ih uw', 'ih aw', 'ih ay', 'ih ey', 'ih ow', 'ih oy', 'ih -', 'iy aa', 'iy ae', 'iy ah', 'iy ao', 'iy ax', 'iy eh', 'iy er', 'iy ih', 'iy iy', 'iy uh', 'iy uw', 'iy aw', 'iy ay', 'iy ey', 'iy ow', 'iy oy', 'iy -', 'uh aa', 'uh ae', 'uh ah', 'uh ao', 'uh ax', 'uh eh', 'uh er', 'uh ih', 'uh iy', 'uh uh', 'uh uw', 'uh aw', 'uh ay', 'uh ey', 'uh ow', 'uh oy', 'uh -', 'uw aa', 'uw ae', 'uw ah', 'uw ao', 'uw ax', 'uw eh', 'uw er', 'uw ih', 'uw iy', 'uw uh', 'uw uw', 'uw aw', 'uw ay', 'uw ey', 'uw ow', 'uw oy', 'uw -', 'aw aa', 'aw ae', 'aw ah', 'aw ao', 'aw ax', 'aw eh', 'aw er', 'aw ih', 'aw iy', 'aw uh', 'aw uw', 'aw aw', 'aw ay', 'aw ey', 'aw ow', 'aw oy', 'aw -', 'ay aa', 'ay ae', 'ay ah', 'ay ao', 'ay ax', 'ay eh', 'ay er', 'ay ih', 'ay iy', 'ay uh', 'ay uw', 'ay aw', 'ay ay', 'ay ey', 'ay ow', 'ay oy', 'ay -', 'ey aa', 'ey ae', 'ey ah', 'ey ao', 'ey ax', 'ey eh', 'ey er', 'ey ih', 'ey iy', 'ey uh', 'ey uw', 'ey aw', 'ey ay', 'ey ey', 'ey ow', 'ey oy', 'ey -', 'ow aa', 'ow ae', 'ow ah', 'ow ao', 'ow ax', 'ow eh', 'ow er', 'ow ih', 'ow iy', 'ow uh', 'ow uw', 'ow aw', 'ow ay', 'ow ey', 'ow ow', 'ow oy', 'ow -', 'oy aa', 'oy ae', 'oy ah', 'oy ao', 'oy ax', 'oy eh', 'oy er', 'oy ih', 'oy iy', 'oy uh', 'oy uw', 'oy aw', 'oy ay', 'oy ey', 'oy ow', 'oy oy', 'oy -', '- aa', '- ae', '- ah', '- ao', '- ax', '- eh', '- er', '- ih', '- iy', '- uh', '- uw', '- aw', '- ay', '- ey', '- ow', '- oy', '- -')
CC_TUPLE = ('b b', 'b ch', 'b d', 'b dh', 'b dx', 'b f', 'b g', 'b hh', 'b jh', 'b k', 'b l', 'b m', 'b n', 'b ng', 'b p', 'b q', 'b r', 'b s', 'b sh', 'b t', 'b th', 'b v', 'b w', 'b y', 'b z', 'b zh', 'ch b', 'ch ch', 'ch d', 'ch dh', 'ch dx', 'ch f', 'ch g', 'ch hh', 'ch jh', 'ch k', 'ch l', 'ch m', 'ch n', 'ch ng', 'ch p', 'ch q', 'ch r', 'ch s', 'ch sh', 'ch t', 'ch th', 'ch v', 'ch w', 'ch y', 'ch z', 'ch zh', 'd b', 'd ch', 'd d', 'd dh', 'd dx', 'd f', 'd g', 'd hh', 'd jh', 'd k', 'd l', 'd m', 'd n', 'd ng', 'd p', 'd q', 'd r', 'd s', 'd sh', 'd t', 'd th', 'd v', 'd w', 'd y', 'd z', 'd zh', 'dh b', 'dh ch', 'dh d', 'dh dh', 'dh dx', 'dh f', 'dh g', 'dh hh', 'dh jh', 'dh k', 'dh l', 'dh m', 'dh n', 'dh ng', 'dh p', 'dh q', 'dh r', 'dh s', 'dh sh', 'dh t', 'dh th', 'dh v', 'dh w', 'dh y', 'dh z', 'dh zh', 'dx b', 'dx ch', 'dx d', 'dx dh', 'dx dx', 'dx f', 'dx g', 'dx hh', 'dx jh', 'dx k', 'dx l', 'dx m', 'dx n', 'dx ng', 'dx p', 'dx q', 'dx r', 'dx s', 'dx sh', 'dx t', 'dx th', 'dx v', 'dx w', 'dx y', 'dx z', 'dx zh', 'f b', 'f ch', 'f d', 'f dh', 'f dx', 'f f', 'f g', 'f hh', 'f jh', 'f k', 'f l', 'f m', 'f n', 'f ng', 'f p', 'f q', 'f r', 'f s', 'f sh', 'f t', 'f th', 'f v', 'f w', 'f y', 'f z', 'f zh', 'g b', 'g ch', 'g d', 'g dh', 'g dx', 'g f', 'g g', 'g hh', 'g jh', 'g k', 'g l', 'g m', 'g n', 'g ng', 'g p', 'g q', 'g r', 'g s', 'g sh', 'g t', 'g th', 'g v', 'g w', 'g y', 'g z', 'g zh', 'hh b', 'hh ch', 'hh d', 'hh dh', 'hh dx', 'hh f', 'hh g', 'hh hh', 'hh jh', 'hh k', 'hh l', 'hh m', 'hh n', 'hh ng', 'hh p', 'hh q', 'hh r', 'hh s', 'hh sh', 'hh t', 'hh th', 'hh v', 'hh w', 'hh y', 'hh z', 'hh zh', 'jh b', 'jh ch', 'jh d', 'jh dh', 'jh dx', 'jh f', 'jh g', 'jh hh', 'jh jh', 'jh k', 'jh l', 'jh m', 'jh n', 'jh ng', 'jh p', 'jh q', 'jh r', 'jh s', 'jh sh', 'jh t', 'jh th', 'jh v', 'jh w', 'jh y', 'jh z', 'jh zh', 'k b', 'k ch', 'k d', 'k dh', 'k dx', 'k f', 'k g', 'k hh', 'k jh', 'k k', 'k l', 'k m', 'k n', 'k ng', 'k p', 'k q', 'k r', 'k s', 'k sh', 'k t', 'k th', 'k v', 'k w', 'k y', 'k z', 'k zh', 'l b', 'l ch', 'l d', 'l dh', 'l dx', 'l f', 'l g', 'l hh', 'l jh', 'l k', 'l l', 'l m', 'l n', 'l ng', 'l p', 'l q', 'l r', 'l s', 'l sh', 'l t', 'l th', 'l v', 'l w', 'l y', 'l z', 'l zh', 'm b', 'm ch', 'm d', 'm dh', 'm dx', 'm f', 'm g', 'm hh', 'm jh', 'm k', 'm l', 'm m', 'm n', 'm ng', 'm p', 'm q', 'm r', 'm s', 'm sh', 'm t', 'm th', 'm v', 'm w', 'm y', 'm z', 'm zh', 'n b', 'n ch', 'n d', 'n dh', 'n dx', 'n f', 'n g', 'n hh', 'n jh', 'n k', 'n l', 'n m', 'n n', 'n ng', 'n p', 'n q', 'n r', 'n s', 'n sh', 'n t', 'n th', 'n v', 'n w', 'n y', 'n z', 'n zh', 'ng b', 'ng ch', 'ng d', 'ng dh', 'ng dx', 'ng f', 'ng g', 'ng hh', 'ng jh', 'ng k', 'ng l', 'ng m', 'ng n', 'ng ng', 'ng p', 'ng q', 'ng r', 'ng s', 'ng sh', 'ng t', 'ng th', 'ng v', 'ng w', 'ng y', 'ng z', 'ng zh', 'p b', 'p ch', 'p d', 'p dh', 'p dx', 'p f', 'p g', 'p hh', 'p jh', 'p k', 'p l', 'p m', 'p n', 'p ng', 'p p', 'p q', 'p r', 'p s', 'p sh', 'p t', 'p th', 'p v', 'p w', 'p y', 'p z', 'p zh', 'q b', 'q ch', 'q d', 'q dh', 'q dx', 'q f', 'q g', 'q hh', 'q jh', 'q k', 'q l', 'q m', 'q n', 'q ng', 'q p', 'q q', 'q r', 'q s', 'q sh', 'q t', 'q th', 'q v', 'q w', 'q y', 'q z', 'q zh', 'r b', 'r ch', 'r d', 'r dh', 'r dx', 'r f', 'r g', 'r hh', 'r jh', 'r k', 'r l', 'r m', 'r n', 'r ng', 'r p', 'r q', 'r r', 'r s', 'r sh', 'r t', 'r th', 'r v', 'r w', 'r y', 'r z', 'r zh', 's b', 's ch', 's d', 's dh', 's dx', 's f', 's g', 's hh', 's jh', 's k', 's l', 's m', 's n', 's ng', 's p', 's q', 's r', 's s', 's sh', 's t', 's th', 's v', 's w', 's y', 's z', 's zh', 'sh b', 'sh ch', 'sh d', 'sh dh', 'sh dx', 'sh f', 'sh g', 'sh hh', 'sh jh', 'sh k', 'sh l', 'sh m', 'sh n', 'sh ng', 'sh p', 'sh q', 'sh r', 'sh s', 'sh sh', 'sh t', 'sh th', 'sh v', 'sh w', 'sh y', 'sh z', 'sh zh', 't b', 't ch', 't d', 't dh', 't dx', 't f', 't g', 't hh', 't jh', 't k', 't l', 't m', 't n', 't ng', 't p', 't q', 't r', 't s', 't sh', 't t', 't th', 't v', 't w', 't y', 't z', 't zh', 'th b', 'th ch', 'th d', 'th dh', 'th dx', 'th f', 'th g', 'th hh', 'th jh', 'th k', 'th l', 'th m', 'th n', 'th ng', 'th p', 'th q', 'th r', 'th s', 'th sh', 'th t', 'th th', 'th v', 'th w', 'th y', 'th z', 'th zh', 'v b', 'v ch', 'v d', 'v dh', 'v dx', 'v f', 'v g', 'v hh', 'v jh', 'v k', 'v l', 'v m', 'v n', 'v ng', 'v p', 'v q', 'v r', 'v s', 'v sh', 'v t', 'v th', 'v v', 'v w', 'v y', 'v z', 'v zh', 'w b', 'w ch', 'w d', 'w dh', 'w dx', 'w f', 'w g', 'w hh', 'w jh', 'w k', 'w l', 'w m', 'w n', 'w ng', 'w p', 'w q', 'w r', 'w s', 'w sh', 'w t', 'w th', 'w v', 'w w', 'w y', 'w z', 'w zh', 'y b', 'y ch', 'y d', 'y dh', 'y dx', 'y f', 'y g', 'y hh', 'y jh', 'y k', 'y l', 'y m', 'y n', 'y ng', 'y p', 'y q', 'y r', 'y s', 'y sh', 'y t', 'y th', 'y v', 'y w', 'y y', 'y z', 'y zh', 'z b', 'z ch', 'z d', 'z dh', 'z dx', 'z f', 'z g', 'z hh', 'z jh', 'z k', 'z l', 'z m', 'z n', 'z ng', 'z p', 'z q', 'z r', 'z s', 'z sh', 'z t', 'z th', 'z v', 'z w', 'z y', 'z z', 'z zh', 'zh b', 'zh ch', 'zh d', 'zh dh', 'zh dx', 'zh f', 'zh g', 'zh hh', 'zh jh', 'zh k', 'zh l', 'zh m', 'zh n', 'zh ng', 'zh p', 'zh q', 'zh r', 'zh s', 'zh sh', 'zh t', 'zh th', 'zh v', 'zh w', 'zh y', 'zh z', 'zh zh')
VC_TUPLE = ('aa b', 'aa ch', 'aa d', 'aa dh', 'aa dx', 'aa f', 'aa g', 'aa hh', 'aa jh', 'aa k', 'aa l', 'aa m', 'aa n', 'aa ng', 'aa p', 'aa q', 'aa r', 'aa s', 'aa sh', 'aa t', 'aa th', 'aa v', 'aa w', 'aa y', 'aa z', 'aa zh', 'ae b', 'ae ch', 'ae d', 'ae dh', 'ae dx', 'ae f', 'ae g', 'ae hh', 'ae jh', 'ae k', 'ae l', 'ae m', 'ae n', 'ae ng', 'ae p', 'ae q', 'ae r', 'ae s', 'ae sh', 'ae t', 'ae th', 'ae v', 'ae w', 'ae y', 'ae z', 'ae zh', 'ah b', 'ah ch', 'ah d', 'ah dh', 'ah dx', 'ah f', 'ah g', 'ah hh', 'ah jh', 'ah k', 'ah l', 'ah m', 'ah n', 'ah ng', 'ah p', 'ah q', 'ah r', 'ah s', 'ah sh', 'ah t', 'ah th', 'ah v', 'ah w', 'ah y', 'ah z', 'ah zh', 'ao b', 'ao ch', 'ao d', 'ao dh', 'ao dx', 'ao f', 'ao g', 'ao hh', 'ao jh', 'ao k', 'ao l', 'ao m', 'ao n', 'ao ng', 'ao p', 'ao q', 'ao r', 'ao s', 'ao sh', 'ao t', 'ao th', 'ao v', 'ao w', 'ao y', 'ao z', 'ao zh', 'ax b', 'ax ch', 'ax d', 'ax dh', 'ax dx', 'ax f', 'ax g', 'ax hh', 'ax jh', 'ax k', 'ax l', 'ax m', 'ax n', 'ax ng', 'ax p', 'ax q', 'ax r', 'ax s', 'ax sh', 'ax t', 'ax th', 'ax v', 'ax w', 'ax y', 'ax z', 'ax zh', 'eh b', 'eh ch', 'eh d', 'eh dh', 'eh dx', 'eh f', 'eh g', 'eh hh', 'eh jh', 'eh k', 'eh l', 'eh m', 'eh n', 'eh ng', 'eh p', 'eh q', 'eh r', 'eh s', 'eh sh', 'eh t', 'eh th', 'eh v', 'eh w', 'eh y', 'eh z', 'eh zh', 'er b', 'er ch', 'er d', 'er dh', 'er dx', 'er f', 'er g', 'er hh', 'er jh', 'er k', 'er l', 'er m', 'er n', 'er ng', 'er p', 'er q', 'er r', 'er s', 'er sh', 'er t', 'er th', 'er v', 'er w', 'er y', 'er z', 'er zh', 'ih b', 'ih ch', 'ih d', 'ih dh', 'ih dx', 'ih f', 'ih g', 'ih hh', 'ih jh', 'ih k', 'ih l', 'ih m', 'ih n', 'ih ng', 'ih p', 'ih q', 'ih r', 'ih s', 'ih sh', 'ih t', 'ih th', 'ih v', 'ih w', 'ih y', 'ih z', 'ih zh', 'iy b', 'iy ch', 'iy d', 'iy dh', 'iy dx', 'iy f', 'iy g', 'iy hh', 'iy jh', 'iy k', 'iy l', 'iy m', 'iy n', 'iy ng', 'iy p', 'iy q', 'iy r', 'iy s', 'iy sh', 'iy t', 'iy th', 'iy v', 'iy w', 'iy y', 'iy z', 'iy zh', 'uh b', 'uh ch', 'uh d', 'uh dh', 'uh dx', 'uh f', 'uh g', 'uh hh', 'uh jh', 'uh k', 'uh l', 'uh m', 'uh n', 'uh ng', 'uh p', 'uh q', 'uh r', 'uh s', 'uh sh', 'uh t', 'uh th', 'uh v', 'uh w', 'uh y', 'uh z', 'uh zh', 'uw b', 'uw ch', 'uw d', 'uw dh', 'uw dx', 'uw f', 'uw g', 'uw hh', 'uw jh', 'uw k', 'uw l', 'uw m', 'uw n', 'uw ng', 'uw p', 'uw q', 'uw r', 'uw s', 'uw sh', 'uw t', 'uw th', 'uw v', 'uw w', 'uw y', 'uw z', 'uw zh', 'aw b', 'aw ch', 'aw d', 'aw dh', 'aw dx', 'aw f', 'aw g', 'aw hh', 'aw jh', 'aw k', 'aw l', 'aw m', 'aw n', 'aw ng', 'aw p', 'aw q', 'aw r', 'aw s', 'aw sh', 'aw t', 'aw th', 'aw v', 'aw w', 'aw y', 'aw z', 'aw zh', 'ay b', 'ay ch', 'ay d', 'ay dh', 'ay dx', 'ay f', 'ay g', 'ay hh', 'ay jh', 'ay k', 'ay l', 'ay m', 'ay n', 'ay ng', 'ay p', 'ay q', 'ay r', 'ay s', 'ay sh', 'ay t', 'ay th', 'ay v', 'ay w', 'ay y', 'ay z', 'ay zh', 'ey b', 'ey ch', 'ey d', 'ey dh', 'ey dx', 'ey f', 'ey g', 'ey hh', 'ey jh', 'ey k', 'ey l', 'ey m', 'ey n', 'ey ng', 'ey p', 'ey q', 'ey r', 'ey s', 'ey sh', 'ey t', 'ey th', 'ey v', 'ey w', 'ey y', 'ey z', 'ey zh', 'ow b', 'ow ch', 'ow d', 'ow dh', 'ow dx', 'ow f', 'ow g', 'ow hh', 'ow jh', 'ow k', 'ow l', 'ow m', 'ow n', 'ow ng', 'ow p', 'ow q', 'ow r', 'ow s', 'ow sh', 'ow t', 'ow th', 'ow v', 'ow w', 'ow y', 'ow z', 'ow zh', 'oy b', 'oy ch', 'oy d', 'oy dh', 'oy dx', 'oy f', 'oy g', 'oy hh', 'oy jh', 'oy k', 'oy l', 'oy m', 'oy n', 'oy ng', 'oy p', 'oy q', 'oy r', 'oy s', 'oy sh', 'oy t', 'oy th', 'oy v', 'oy w', 'oy y', 'oy z', 'oy zh', '- b', '- ch', '- d', '- dh', '- dx', '- f', '- g', '- hh', '- jh', '- k', '- l', '- m', '- n', '- ng', '- p', '- q', '- r', '- s', '- sh', '- t', '- th', '- v', '- w', '- y', '- z', '- zh')
CV_TUPLE = ('b aa', 'b ae', 'b ah', 'b ao', 'b ax', 'b eh', 'b er', 'b ih', 'b iy', 'b uh', 'b uw', 'b aw', 'b ay', 'b ey', 'b ow', 'b oy', 'b -', 'ch aa', 'ch ae', 'ch ah', 'ch ao', 'ch ax', 'ch eh', 'ch er', 'ch ih', 'ch iy', 'ch uh', 'ch uw', 'ch aw', 'ch ay', 'ch ey', 'ch ow', 'ch oy', 'ch -', 'd aa', 'd ae', 'd ah', 'd ao', 'd ax', 'd eh', 'd er', 'd ih', 'd iy', 'd uh', 'd uw', 'd aw', 'd ay', 'd ey', 'd ow', 'd oy', 'd -', 'dh aa', 'dh ae', 'dh ah', 'dh ao', 'dh ax', 'dh eh', 'dh er', 'dh ih', 'dh iy', 'dh uh', 'dh uw', 'dh aw', 'dh ay', 'dh ey', 'dh ow', 'dh oy', 'dh -', 'dx aa', 'dx ae', 'dx ah', 'dx ao', 'dx ax', 'dx eh', 'dx er', 'dx ih', 'dx iy', 'dx uh', 'dx uw', 'dx aw', 'dx ay', 'dx ey', 'dx ow', 'dx oy', 'dx -', 'f aa', 'f ae', 'f ah', 'f ao', 'f ax', 'f eh', 'f er', 'f ih', 'f iy', 'f uh', 'f uw', 'f aw', 'f ay', 'f ey', 'f ow', 'f oy', 'f -', 'g aa', 'g ae', 'g ah', 'g ao', 'g ax', 'g eh', 'g er', 'g ih', 'g iy', 'g uh', 'g uw', 'g aw', 'g ay', 'g ey', 'g ow', 'g oy', 'g -', 'hh aa', 'hh ae', 'hh ah', 'hh ao', 'hh ax', 'hh eh', 'hh er', 'hh ih', 'hh iy', 'hh uh', 'hh uw', 'hh aw', 'hh ay', 'hh ey', 'hh ow', 'hh oy', 'hh -', 'jh aa', 'jh ae', 'jh ah', 'jh ao', 'jh ax', 'jh eh', 'jh er', 'jh ih', 'jh iy', 'jh uh', 'jh uw', 'jh aw', 'jh ay', 'jh ey', 'jh ow', 'jh oy', 'jh -', 'k aa', 'k ae', 'k ah', 'k ao', 'k ax', 'k eh', 'k er', 'k ih', 'k iy', 'k uh', 'k uw', 'k aw', 'k ay', 'k ey', 'k ow', 'k oy', 'k -', 'l aa', 'l ae', 'l ah', 'l ao', 'l ax', 'l eh', 'l er', 'l ih', 'l iy', 'l uh', 'l uw', 'l aw', 'l ay', 'l ey', 'l ow', 'l oy', 'l -', 'm aa', 'm ae', 'm ah', 'm ao', 'm ax', 'm eh', 'm er', 'm ih', 'm iy', 'm uh', 'm uw', 'm aw', 'm ay', 'm ey', 'm ow', 'm oy', 'm -', 'n aa', 'n ae', 'n ah', 'n ao', 'n ax', 'n eh', 'n er', 'n ih', 'n iy', 'n uh', 'n uw', 'n aw', 'n ay', 'n ey', 'n ow', 'n oy', 'n -', 'ng aa', 'ng ae', 'ng ah', 'ng ao', 'ng ax', 'ng eh', 'ng er', 'ng ih', 'ng iy', 'ng uh', 'ng uw', 'ng aw', 'ng ay', 'ng ey', 'ng ow', 'ng oy', 'ng -', 'p aa', 'p ae', 'p ah', 'p ao', 'p ax', 'p eh', 'p er', 'p ih', 'p iy', 'p uh', 'p uw', 'p aw', 'p ay', 'p ey', 'p ow', 'p oy', 'p -', 'q aa', 'q ae', 'q ah', 'q ao', 'q ax', 'q eh', 'q er', 'q ih', 'q iy', 'q uh', 'q uw', 'q aw', 'q ay', 'q ey', 'q ow', 'q oy', 'q -', 'r aa', 'r ae', 'r ah', 'r ao', 'r ax', 'r eh', 'r er', 'r ih', 'r iy', 'r uh', 'r uw', 'r aw', 'r ay', 'r ey', 'r ow', 'r oy', 'r -', 's aa', 's ae', 's ah', 's ao', 's ax', 's eh', 's er', 's ih', 's iy', 's uh', 's uw', 's aw', 's ay', 's ey', 's ow', 's oy', 's -', 'sh aa', 'sh ae', 'sh ah', 'sh ao', 'sh ax', 'sh eh', 'sh er', 'sh ih', 'sh iy', 'sh uh', 'sh uw', 'sh aw', 'sh ay', 'sh ey', 'sh ow', 'sh oy', 'sh -', 't aa', 't ae', 't ah', 't ao', 't ax', 't eh', 't er', 't ih', 't iy', 't uh', 't uw', 't aw', 't ay', 't ey', 't ow', 't oy', 't -', 'th aa', 'th ae', 'th ah', 'th ao', 'th ax', 'th eh', 'th er', 'th ih', 'th iy', 'th uh', 'th uw', 'th aw', 'th ay', 'th ey', 'th ow', 'th oy', 'th -', 'v aa', 'v ae', 'v ah', 'v ao', 'v ax', 'v eh', 'v er', 'v ih', 'v iy', 'v uh', 'v uw', 'v aw', 'v ay', 'v ey', 'v ow', 'v oy', 'v -', 'w aa', 'w ae', 'w ah', 'w ao', 'w ax', 'w eh', 'w er', 'w ih', 'w iy', 'w uh', 'w uw', 'w aw', 'w ay', 'w ey', 'w ow', 'w oy', 'w -', 'y aa', 'y ae', 'y ah', 'y ao', 'y ax', 'y eh', 'y er', 'y ih', 'y iy', 'y uh', 'y uw', 'y aw', 'y ay', 'y ey', 'y ow', 'y oy', 'y -', 'z aa', 'z ae', 'z ah', 'z ao', 'z ax', 'z eh', 'z er', 'z ih', 'z iy', 'z uh', 'z uw', 'z aw', 'z ay', 'z ey', 'z ow', 'z oy', 'z -', 'zh aa', 'zh ae', 'zh ah', 'zh ao', 'zh ax', 'zh eh', 'zh er', 'zh ih', 'zh iy', 'zh uh', 'zh uw', 'zh aw', 'zh ay', 'zh ey', 'zh ow', 'zh oy', 'zh -')
V = []
C = []
VC = []
CV = []
VV = []
CC = []
NPF = []

start = BooleanVar(value=False)

filename = 0
dirname = 0

combo_found = 0

def disable():
    pass
root.protocol('WM_DELETE_WINDOW', disable)

def askfor_oto(func):
    global filename
    filename = fd.askopenfilename(initialdir="/", title="Select oto.ini file", filetypes=(("Config files", "*.ini"), ("Text files", "*.txt")))

    if len(str(filename)) > 80:
        func.configure(text="oto.ini file path : " + str(filename)[:80] + "...")
    else:
        func.configure(text="oto.ini file path : " + str(filename))

def askfor_split(func):
    global dirname
    dirname = fd.askdirectory(initialdir="/", title="Select output folder")
    
    if len(str(dirname)) > 76:
        func.configure(text="Output folder path : " + str(dirname)[:76] + "...")
    else:
        func.configure(text="Output folder path : " + str(dirname))

def checkforcombo(phonemetuple, appendlist):
    for index in range(len(phonemetuple)):
        if phonemetuple[index] == oto_fix:
            appendlist.append(oto_con[line_number])
            index = 0
            global combo_found
            combo_found = True

def egress():
    time.sleep(0.10)
    os._exit(0)


############################################################### --- setting up buttons and labels



exit_button = Button(root, text="Exit", background="#FF0000", foreground="#FFFFFF", command=lambda: egress())
exit_button.place(x=0, y=0)

oto_status = ttk.Label(root, text="No oto.ini file selected", background="#FFFFFF")
split_status = ttk.Label(root, text="No output folder selected", background="#FFFFFF")
prog_status = ttk.Label(root, text="Program not started", background="#FFFFFF", relief=SUNKEN, padding=5)

oto_button = Button(root, text="Browse for oto.ini file", width=38, command=lambda: askfor_oto(oto_status))
split_button = Button(root, text="Browse for output folder", width=38, command=lambda: askfor_split(split_status))
start_button = Button(root, text="Start Program", width=20, command=lambda: start.set(True))

oto_button.place(x=20, y=120)
split_button.place(x=300, y=120)

oto_status.place(x=20, y=150)
split_status.place(x=20, y=170)

start_button.place(x=20, y=200) #x=225 for center
prog_status.place(x=175, y=200)



############################################################### --- actual program stuff, most is just copied from the nogui version, so i deleted all the comments and stuff cuz it functions pretty much the exact same



root.wait_variable(start)

if filename == 0:
    prog_status.configure(text="No oto.ini file selected. Program terminating in 3 seconds to avoid an error.")
    root.update()
    time.sleep(3)
    sys.exit()
if dirname == 0:
    prog_status.configure(text="No output folder selected. Program terminating in 3 seconds to avoid an error.", padding=3)
    root.update()
    time.sleep(3)
    sys.exit()

oto_con = open(str(filename), "r").readlines()
v_ = open(dirname + "/oto-v.txt", "w")
c_ = open(dirname + "/oto-c.txt", "w")
vc_ = open(dirname + "/oto-vc.txt", "w")
cv_ = open(dirname + "/oto-cv.txt", "w")
vv_ = open(dirname + "/oto-vv.txt", "w")
cc_ = open(dirname + "/oto-cc.txt", "w")
npf_ = open(dirname + "/oto-_no_phonemes_found.txt", "w")

for line_number in range(len(oto_con)):
    root.update()
    prog_status.configure(text="Don't close the window, currently on Entry " + str(line_number))

    combo_found = False

    oto_fix = "".join((z for z in oto_con[line_number][oto_con[line_number].find("=") + 3:oto_con[line_number].find(",")] if not z.isdigit()))

    checkforcombo(VV_TUPLE, VV)
    if combo_found == True: continue
    checkforcombo(CC_TUPLE, CC)
    if combo_found == True: continue
    checkforcombo(VC_TUPLE, VC)
    if combo_found == True: continue
    checkforcombo(CV_TUPLE, CV)
    if combo_found == True: continue
    checkforcombo(V_TUPLE, V)
    if combo_found == True: continue
    checkforcombo(C_TUPLE, C)
    if combo_found == True: continue
    else: NPF.append(oto_con[line_number])



############################################################### --- write to text files then quit



v_.writelines(V)
c_.writelines(C)
vc_.writelines(VC)
cv_.writelines(CV)
vv_.writelines(VV)
cc_.writelines(CC)
npf_.writelines(NPF)

v_.close()
c_.close()
vc_.close()
cv_.close()
vv_.close()
cc_.close()
npf_.close()
prog_status.configure(text="Program complete, you may now close the window")
root.mainloop()