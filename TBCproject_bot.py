import os
import logging
import requests
from bs4 import BeautifulSoup
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,  
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)



#####################################################################################################################################

abc = {
    '1':'Azarbaijan_sharghi', '2':'Azarbaijan_gharbi', '3':'Ardabil', '4':'Isfahan', '5':'Alborz', '6':'Ilam', '7':'Bushehr', '8':'Tehran', '9':'Chaharmahaal_va_bakhtiari',
        '10':'Khorasan_jonobi', '11':'Khorasan_razavi', '12':'Khorasan_shomali', '13':'Khuzestan', '14':'Zanjan', '15':'Semnan', '16':'Sistan_va_baluchestan',
        '17':'Fars', '18':'Qazvin', '19':'Qom', '20':'Kordestan', '21':'Kerman', '22':'Kermanshah', '23':'Kohgiluyeh_va_boyer_ahmad',
         '24':'Golestan', '25':'Gilan', '26':'Lorestan', '27':'Mazandaran', '28':'Markazi', '29':'Hormozgan', '30':'Hamadan', '31':'Yazd',     
}

###########################################################################################################
mydict = {}
my_id = ''
ostan, shahr, option, min1, max1, time1 = range(6)

def start(update: Update, context: CallbackContext) -> None:
    """Send message on `/start`."""


    global my_id, mydict
    name_id = update.message.from_user.id
    my_id = str(name_id)
    mydict[my_id] = {}

    keyboard = [
        [
            InlineKeyboardButton("آذربایجان شرقی", callback_data='@1'),
            InlineKeyboardButton("آذربایجان غربی", callback_data='@2'),
            InlineKeyboardButton("اردبیل", callback_data='@3'),  
            InlineKeyboardButton("اصفهان", callback_data='@4'),          
        ],
        [
            InlineKeyboardButton("البرز", callback_data='@5'),
            InlineKeyboardButton("ایلام", callback_data='@6'),           
            InlineKeyboardButton("بوشهر", callback_data='@7'),   
            InlineKeyboardButton("تهران", callback_data='@8'),        
        ],
        [
            InlineKeyboardButton("چهارمحال و بختیاری", callback_data='@9'),
            InlineKeyboardButton("خراسان جنوبی", callback_data='#10'),           
            InlineKeyboardButton("خراسان رضوی", callback_data='#11'),   
            InlineKeyboardButton("خراسان شمالی", callback_data='#12'),        
        ],
        [
            InlineKeyboardButton("خوزستان", callback_data='#13'),
            InlineKeyboardButton("زنجان", callback_data='#14'),           
            InlineKeyboardButton("سمنان", callback_data='#15'),   
            InlineKeyboardButton("سیستان و بلوچستان", callback_data='#16'),        
        ],
        [
            InlineKeyboardButton("فارس", callback_data='#17'),
            InlineKeyboardButton("قزوین", callback_data='#18'),           
            InlineKeyboardButton("قم", callback_data='#19'),   
            InlineKeyboardButton("کردستان", callback_data='#20'),        
        ],
        [
            InlineKeyboardButton("کرمان", callback_data='!21'),
            InlineKeyboardButton("کرمانشاه", callback_data='!22'),           
            InlineKeyboardButton("کهگیلویه و بویراحمد", callback_data='!23'),   
            InlineKeyboardButton("گلستان", callback_data='!24'),        
        ],
        [
            InlineKeyboardButton("گیلان", callback_data='!25'),
            InlineKeyboardButton("لرستان", callback_data='!26'),           
            InlineKeyboardButton("مازندران", callback_data='!27'),   
            InlineKeyboardButton("مرکزی", callback_data='!28'),        
        ],

        [
            InlineKeyboardButton("هرمزگان", callback_data='!29'),
            InlineKeyboardButton("همدان", callback_data='!30'),           
            InlineKeyboardButton("یزد", callback_data='%31'),           
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(' سلام. به @TBCproject_bot خوش آمدید! لطفا یکی از استان های مورد نظر را انتخاب نمایید', reply_markup=reply_markup)
    return ostan

#################################################################################################################################


def help(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text(
        "اين بات به منظور سهولت در يافتن موارد دلخواه شما تشکيل شده است.\nروش کار آن به این صورت است که با دریافت اطلاعات لازم برای شناسایی آگهی مدنظر شما، پس از بررسی و تطابق دادن، آن موارد برای شما ارسال می گردد.\nبراي شروع /start را انتخاب کنيد."    
    )


#######################################################################################################################################


def Time(update: Update, context: CallbackContext) -> None:
    """Send message on `/Qom`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("یک ساعت گذشته", callback_data='1 ساعت'), 
                 
        ],
        [
            InlineKeyboardButton("دو ساعت گذشته", callback_data='2 ساعت')   
                                                      
        ], 
        [
            InlineKeyboardButton("سه ساعت گذشته", callback_data='3 ساعت')                                              
        ],                                              
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا حداکثر ساعت ثبت شده آگهی مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    if str(query.data) == 'jobs' or str(query.data) == 'services':
        mydict[my_id]['option'] = str(query.data)
    else:
        mydict[my_id]['max'] = int(query.data) 
    return time1


#######################################################################################################################################


def Qom(update: Update, context: CallbackContext) -> None:
    """Send message on `/Qom`."""
    global my_id, mydict

    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("قم", callback_data='qom'),                                           
        ],                                       
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:]
    return shahr


#######################################################################################################################################


def Sistan_va_baluchestan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Sistan_va_baluchestan`."""
    global my_id, mydict

    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='sistan-and-baluchestan-province'),        
        ],
        [
            InlineKeyboardButton("ایرانشهر", callback_data='iranshahr'),
            InlineKeyboardButton("چابهار", callback_data='chabahar'),  
            InlineKeyboardButton("زابل", callback_data='zabol'),                                             
        ],
        [
            InlineKeyboardButton("زاهدان", callback_data='zahedan'),
            InlineKeyboardButton("سراوان", callback_data='saravan'),                              
        ],                                
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:]  
    return shahr


#######################################################################################################################################


def Fars(update: Update, context: CallbackContext) -> None:
    """Send message on `/Fars`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='fars-province'),        
        ],
        [
            InlineKeyboardButton("آباده", callback_data='abadeh'),
            InlineKeyboardButton("اقلید", callback_data='eqlid'),  
            InlineKeyboardButton("جهرم", callback_data='jahrom'),                                             
        ],
        [
            InlineKeyboardButton("داراب", callback_data='darab'),
            InlineKeyboardButton("شیراز", callback_data='shiraz'), 
            InlineKeyboardButton("صدرا", callback_data='sadra'),                                         
        ],                               
        [
            InlineKeyboardButton("لار", callback_data='lar'),
            InlineKeyboardButton("لامرد", callback_data='lamerd'), 
            InlineKeyboardButton("نی ریز", callback_data='neyriz'),                                         
        ],         
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Zanjan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Zanjan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='zanjan-province'),        
        ],
        [
            InlineKeyboardButton("ابهر", callback_data='abhar'),
            InlineKeyboardButton("خرمدره", callback_data='khorramdarreh'),                                  
        ],
        [
            InlineKeyboardButton("زنجان", callback_data='zanjan'),
            InlineKeyboardButton("قیدار", callback_data='qeydar'),                              
        ],                                
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Chaharmahaal_va_bakhtiari(update: Update, context: CallbackContext) -> None:
    """Send message on `/Chaharmahaal_va_bakhtiari`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='chahar-mahaal-and-bakhtiari-province'),        
        ],
        [
            InlineKeyboardButton("بروجن", callback_data='boroujen'),
            InlineKeyboardButton("شهرکرد", callback_data='shahrekord'),            
        ],
        [
            InlineKeyboardButton("فرخ شهر", callback_data='farrokhshahr'),
            InlineKeyboardButton("لردگان", callback_data='lordegan'),       
        ],   
              
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Semnan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Semnan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='semnan-province'),        
        ],
        [
            InlineKeyboardButton("دامغان", callback_data='damghan'),
            InlineKeyboardButton("سمنان", callback_data='semnan'),                                  
        ],
        [
            InlineKeyboardButton("شاهرود", callback_data='shahroud'),
            InlineKeyboardButton("گرمسار", callback_data='garmsar'),                              
        ],                                
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Golestan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Golestan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='golestan-province'),        
        ],
        [
            InlineKeyboardButton("آزادشهر", callback_data='azadshahr-golestan'), 
            InlineKeyboardButton("آق قلا", callback_data='aq-qala'),   
            InlineKeyboardButton("بندر ترکمن", callback_data='bandar-torkaman'), 
            InlineKeyboardButton("علی آباد کتول", callback_data='aliabad-katul'),                                                                            
        ], 
        [
            InlineKeyboardButton("کردکوی", callback_data='kordkuy'), 
            InlineKeyboardButton("کلاله", callback_data='kalale'),  
            InlineKeyboardButton("گرگان", callback_data='gorgan'), 
            InlineKeyboardButton("گمیشان", callback_data='gomishan'),                                                                             
        ],
        [
            InlineKeyboardButton("گنبدکاووس", callback_data='gonbad-kavus'), 
            InlineKeyboardButton("مینودشت", callback_data='minoodasht'),                                                                 
        ],                                                      
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Khorasan_razavi(update: Update, context: CallbackContext) -> None:
    """Send message on `/khorasan-razavi`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='horasan-razavi-province'),        
        ],
        [
            InlineKeyboardButton("بردسکن", callback_data='bardaskan'),
            InlineKeyboardButton("تایباد", callback_data='taybad'),  
            InlineKeyboardButton("تربت جام", callback_data='torbat-jam'),
            InlineKeyboardButton("چناران", callback_data='chenaran'),                      
        ],
        [
            InlineKeyboardButton("خواف", callback_data='khaf'),
            InlineKeyboardButton("سبزوار", callback_data='sabzevar'),  
            InlineKeyboardButton("قاسم آباد", callback_data='qasemabad-khaf'),
            InlineKeyboardButton("گناباد", callback_data='gonabad'),                 
        ],      
        [
            InlineKeyboardButton("مشهد", callback_data='mashhad'),
            InlineKeyboardButton("نیشابور", callback_data='neyshabur'),                 
        ],             
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Qazvin(update: Update, context: CallbackContext) -> None:
    """Send message on `/Qazvin`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='qazvin-province'),        
        ],
        [
            InlineKeyboardButton("آبیک", callback_data='abyek'),
            InlineKeyboardButton("الوند", callback_data='alvand'),  
            InlineKeyboardButton("تاکستان", callback_data='takestan'),                                             
        ],
        [
            InlineKeyboardButton("قزوین", callback_data='qazvin'),
            InlineKeyboardButton("محمدیه", callback_data='mohammadiyeh'),                                      
        ],                                        
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Kohgiluyeh_va_boyer_ahmad(update: Update, context: CallbackContext) -> None:
    """Send message on `/Kohgiluyeh_va_boyer_ahmad`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='kohgiluyeh-and-boyer-ahmad-province'),        
        ],
        [
            InlineKeyboardButton("دوگنبدان", callback_data='dogonbadan'), 
            InlineKeyboardButton("دهدشت", callback_data='dehdasht'),                                                                 
        ], 
        [
            InlineKeyboardButton("یاسوج", callback_data='yasuj'),                  
        ],                                              
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Khorasan_jonobi(update: Update, context: CallbackContext) -> None:
    """Send message on `/Khorasan_jonobi`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='khorasan-south-province'),        
        ],
        [
            InlineKeyboardButton("بیرجند", callback_data='birjand'),
            InlineKeyboardButton("طبس", callback_data='tabas'),            
        ],
        [
            InlineKeyboardButton("فردوس", callback_data='ferdows'),
            InlineKeyboardButton("قاین", callback_data='ghayen'),       
        ],         
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Kordestan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Kordestan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='kurdistan-province'),        
        ],
        [
            InlineKeyboardButton("بانه", callback_data='baneh'), 
            InlineKeyboardButton("بیجار", callback_data='bijar'), 
            InlineKeyboardButton("سقز", callback_data='saqqez'),                                                                   
        ], 
        [
            InlineKeyboardButton("سنندج", callback_data='sanandaj'), 
            InlineKeyboardButton("قروه", callback_data='qorveh'), 
            InlineKeyboardButton("مریوان", callback_data='marivan'),                                           
        ],                                              
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Hormozgan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Hormozgan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='hormozgan-province'),        
        ],
        [
            InlineKeyboardButton("بندرعباس", callback_data='bandar-abbas'), 
            InlineKeyboardButton("قشم", callback_data='qeshm'),                                                                            
        ],
        [
            InlineKeyboardButton("کیش", callback_data='kish'), 
            InlineKeyboardButton("میناب", callback_data='minab'),                                                                              
        ],                                                                     
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Mazandaran(update: Update, context: CallbackContext) -> None:
    """Send message on `/Mazandaran`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='mazandaran-province'),        
        ],
        [
            InlineKeyboardButton("آمل", callback_data='amol'), 
            InlineKeyboardButton("امیرکلا", callback_data='amirkala'),  
            InlineKeyboardButton("ایزدشهر", callback_data='izadshahr'), 
            InlineKeyboardButton("بابل", callback_data='babol'),                                                                             
        ],
        [
            InlineKeyboardButton("بابلسر", callback_data='babolsar'), 
            InlineKeyboardButton("بهشهر", callback_data='behshahr'),  
            InlineKeyboardButton("پل سفید", callback_data='polsefid'), 
            InlineKeyboardButton("تنکابن", callback_data='tonekabon'),                                                                             
        ],       
        [
            InlineKeyboardButton("جویبار", callback_data='juybar'), 
            InlineKeyboardButton("چالوس", callback_data='chalus'),  
            InlineKeyboardButton("چمستان", callback_data='chamestan'), 
            InlineKeyboardButton("رامسر", callback_data='ramsar'),                                                                             
        ],
        [
            InlineKeyboardButton("رویان", callback_data='royan'), 
            InlineKeyboardButton("ساری", callback_data='sari'),  
            InlineKeyboardButton("سرخرود", callback_data='sorkhrood'), 
            InlineKeyboardButton("سلمان شهر", callback_data='salman-shahr'),                                                                             
        ],
        [
            InlineKeyboardButton("عباس آباد", callback_data='abbasabad-mazandaran'), 
            InlineKeyboardButton("فریدون کنار", callback_data='fereydunkenar'),  
            InlineKeyboardButton("قایم شهر", callback_data='qaemshahr'), 
            InlineKeyboardButton("کلارآباد", callback_data='kelarabad'),                                                                             
        ],
        [
            InlineKeyboardButton("کلاردشت", callback_data='kelarestan'), 
            InlineKeyboardButton("محمودآباد", callback_data='mahmudabad'),  
            InlineKeyboardButton("نکا", callback_data='neka'),                                                                             
        ],
        [
            InlineKeyboardButton("نور", callback_data='nur'), 
            InlineKeyboardButton("نوشهر", callback_data='nowshahr'),                                                                             
        ],                                                                
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Kerman(update: Update, context: CallbackContext) -> None:
    """Send message on `/Kerman`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='kerman-province'),        
        ],
        [
            InlineKeyboardButton("بم", callback_data='bam'), 
            InlineKeyboardButton("جیرفت", callback_data='jiroft'), 
            InlineKeyboardButton("رفسنجان", callback_data='rafsanjan'),                                                                   
        ], 
        [
            InlineKeyboardButton("زرند", callback_data='zarand'), 
            InlineKeyboardButton("سیرجان", callback_data='sirjan'), 
            InlineKeyboardButton("کرمان", callback_data='kerman'),                                           
        ],                                              
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Hamadan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Hamadan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='hamadan-province'),        
        ],
        [
            InlineKeyboardButton("اسدآباد", callback_data='asadabad'), 
            InlineKeyboardButton("تویسرکان", callback_data='tuyserkan'), 
            InlineKeyboardButton("ملایر", callback_data='malayer'),                                                                                       
        ],
        [
            InlineKeyboardButton("نهاوند", callback_data='nahavand'), 
            InlineKeyboardButton("همدان", callback_data='hamedan'),                                                                              
        ],                                                                     
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Markazi(update: Update, context: CallbackContext) -> None:
    """Send message on `/Markazi`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='markazi-province'),        
        ],
        [
            InlineKeyboardButton("اراک", callback_data='arak'), 
            InlineKeyboardButton("خمین", callback_data='khomein'),                                                                            
        ],
        [
            InlineKeyboardButton("ساوه", callback_data='saveh'), 
            InlineKeyboardButton("محلات", callback_data='mahalat'),                                                                              
        ],                                                                     
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Khorasan_shomali(update: Update, context: CallbackContext) -> None:
    """Send message on `/Khorasan_shomali`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='khorasan-north-province'),        
        ],
        [
            InlineKeyboardButton("آشخانه", callback_data='ashkhaneh'),
            InlineKeyboardButton("اسفراین", callback_data='esfarāyen'),                       
        ],
        [
            InlineKeyboardButton("بجنورد", callback_data='bojnurd'),
            InlineKeyboardButton("شیروان", callback_data='shirvan'),                  
        ],                  
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Lorestan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Lorestan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='lorestan-province'),        
        ],
        [
            InlineKeyboardButton("ازنا", callback_data='azna'), 
            InlineKeyboardButton("الیگودرز", callback_data='aligudarz'),  
            InlineKeyboardButton("بروجرد", callback_data='borujerd'), 
            InlineKeyboardButton("خرم آباد", callback_data='khorramabad'),                                                                             
        ],
        [
            InlineKeyboardButton("دورود", callback_data='dorud'), 
            InlineKeyboardButton("کوهدشت", callback_data='kuhdasht'),  
            InlineKeyboardButton("نورآباد", callback_data='nurabad'),                                                                             
        ],                                                                 
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Gilan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Golestan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='gilan-province'),        
        ],
        [
            InlineKeyboardButton("آستارا", callback_data='astara'), 
            InlineKeyboardButton("آستانه اشرفیه", callback_data='astaneh-ashrafiyeh'),  
            InlineKeyboardButton("املش", callback_data='amlash'), 
            InlineKeyboardButton("بندرانزلی", callback_data='bandar-anzali'),                                                                             
        ],
        [
            InlineKeyboardButton("تالش", callback_data='talesh'), 
            InlineKeyboardButton("چابکسر", callback_data='chaboksar'),  
            InlineKeyboardButton("چاف و جمخاله", callback_data='chaf-chamkhale'), 
            InlineKeyboardButton("خشکبیجار", callback_data='khoshkbijar'),                                                                             
        ],
        [
            InlineKeyboardButton("رشت", callback_data='rasht'), 
            InlineKeyboardButton("رضوانشهر", callback_data='rezvanshahr'),  
            InlineKeyboardButton("زیباکنار", callback_data='zibakenar'), 
            InlineKeyboardButton("رودسر", callback_data='rudsar'),                                                                             
        ],       
        [
            InlineKeyboardButton("سیاهکل", callback_data='siahkal'), 
            InlineKeyboardButton("صومعه", callback_data='someh-sara'),  
            InlineKeyboardButton("فومن", callback_data='doggorganonbadan'), 
            InlineKeyboardButton("کلاچای", callback_data='kelachay'),                                                                                        
        ],  
        [ 
            InlineKeyboardButton("کیاشهر", callback_data='kiashahr'), 
            InlineKeyboardButton("لاهیجان", callback_data='lahijan'),  
            InlineKeyboardButton("لشت نشا", callback_data='lashtenesha'),                                                                                          
        ],  
        [ 
            InlineKeyboardButton("لنگرود", callback_data='langarud'), 
            InlineKeyboardButton("ماسال", callback_data='masal'),                                                                                           
        ],                                                                          
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################



def Bushehr(update: Update, context: CallbackContext) -> None:
    """Send message on `/Bushehr`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='bushehr-province'),        
        ],
        [
            InlineKeyboardButton("برازجان", callback_data='borazjan'),
            InlineKeyboardButton("بندر کنگان", callback_data='bandar-kangan'), 
        ],
        [
            InlineKeyboardButton("بندر گناوه", callback_data='bandar-ganaveh'),
            InlineKeyboardButton("بوشهر", callback_data='bushehr'), 
        ],
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr

#######################################################################################################################################


def Tehran(update: Update, context: CallbackContext) -> None:
    """Send message on `/Tehran`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='tehran-province'),        
        ],
        [
            InlineKeyboardButton("آبسرد", callback_data='absard'),
            InlineKeyboardButton("آبعلی", callback_data='abali'), 
            InlineKeyboardButton("ارجمند", callback_data='arjmand'),
            InlineKeyboardButton("اسلام شهر", callback_data='eslamshahr'),            
        ],
        [
            InlineKeyboardButton("باقرشهر", callback_data='baghershahr'),
            InlineKeyboardButton("پیشوا", callback_data='pishva'),
            InlineKeyboardButton("تهران", callback_data='tehran'),
            InlineKeyboardButton("جوادآباد", callback_data='javadabad'),             
        ],
        [
            InlineKeyboardButton("چهاردانگه", callback_data='chahar-dangeh'),
            InlineKeyboardButton("دماوند", callback_data='damavand'),
            InlineKeyboardButton("شاهدشهر", callback_data='shahedshahr'),
            InlineKeyboardButton("شمشک", callback_data='shemshak'),             
        ],  
        [
            InlineKeyboardButton("صباشهر", callback_data='sabashahr'),
            InlineKeyboardButton("صفادشت", callback_data='safadasht-industrial-city'),
            InlineKeyboardButton("فردوسیه", callback_data='ferdosiye'),
            InlineKeyboardButton("کهریزک", callback_data='kahrizak'),             
        ],              
        [
            InlineKeyboardButton("کیلان", callback_data='kilan'),
            InlineKeyboardButton("گلستان", callback_data='golestan-baharestan'),
            InlineKeyboardButton("نسیم شهر", callback_data='nasimshahr'),
            InlineKeyboardButton("وحیدیه", callback_data='vahidieh'),             
        ],           
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr



#######################################################################################################################################


def Khuzestan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Khuzestan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='khuzestan-province'),        
        ],
        [
            InlineKeyboardButton("آبادان", callback_data='abadan'),
            InlineKeyboardButton("اندیمشک", callback_data='andimeshk'),  
            InlineKeyboardButton("اهواز", callback_data='ahvaz'),
            InlineKeyboardButton("ایذه", callback_data='izeh'),                                 
        ],
        [
            InlineKeyboardButton("بندر امام خمینی", callback_data='bandar-imam-khomeini'),
            InlineKeyboardButton("بندر ماهشهر", callback_data='bandar-mahshahr'),  
            InlineKeyboardButton("بهبهان", callback_data='behbahan'),
            InlineKeyboardButton("خرمشهر", callback_data='khorramshahr'),                            
        ],       
        [
            InlineKeyboardButton("دزفول", callback_data='dezful'),
            InlineKeyboardButton("رامهرمز", callback_data='ramhormoz'),  
            InlineKeyboardButton("سوسنگرد", callback_data='susangerd'),
            InlineKeyboardButton("شوش", callback_data='shush'),                            
        ], 
        [
            InlineKeyboardButton("شوشتر", callback_data='shooshtar'),
            InlineKeyboardButton("مسجد سلیمان", callback_data='masjed-soleyman'),                              
        ],                                
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr

#######################################################################################################################################


def Ilam(update: Update, context: CallbackContext) -> None:
    """Send message on `/Ilam`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='ilam-province'),        
        ],
        [
            InlineKeyboardButton("آبدانان", callback_data='abdanan'),
            InlineKeyboardButton("ایلام", callback_data='ilam'), 
        ],
        [
            InlineKeyboardButton("ایوان", callback_data='eyvan'),
            InlineKeyboardButton("دهلران", callback_data='dehloran'), 
        ],
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Kermanshah(update: Update, context: CallbackContext) -> None:
    """Send message on `/Kermanshah`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='kermanshah-province'),        
        ],
        [
            InlineKeyboardButton("اسلام آباد غرب", callback_data='eslamabad-gharb'), 
            InlineKeyboardButton("جوانرود", callback_data='javanrud'), 
            InlineKeyboardButton("سرپل ذهاب", callback_data='sarpol-zahab'),                                                                   
        ], 
        [
            InlineKeyboardButton("سنقر", callback_data='sonqor'), 
            InlineKeyboardButton("کرمانشاه", callback_data='Kermanshah'), 
            InlineKeyboardButton("کنگاور", callback_data='kangavar'),                                           
        ],                                              
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Alborz(update: Update, context: CallbackContext) -> None:
    """Send message on `/Alborz`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='alborz-province'),        
        ],
        [
            InlineKeyboardButton("آسارا", callback_data='asara'),
            InlineKeyboardButton("اشتهارد", callback_data='eshtehard'), 
            InlineKeyboardButton("تنکمان", callback_data='tankaman'), 
        ],
        [
            InlineKeyboardButton("چهارباغ", callback_data='charbagh-alborz'),
            InlineKeyboardButton("طالقان", callback_data='taleqan'), 
            InlineKeyboardButton("کرج", callback_data='karaj'), 
        ],
        [
            InlineKeyboardButton("کوهشهر", callback_data='koohsar'),
            InlineKeyboardButton("گرمدره", callback_data='garmdareh'),
            InlineKeyboardButton("نظرآباد", callback_data='nazarabad'),              
        ],
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################


def Isfahan(update: Update, context: CallbackContext) -> None:
    """Send message on `/Isfahan`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='isfahan-province'),        
        ],
        [
            InlineKeyboardButton("آران و بیدگل", callback_data='aran-va-bidgol'),
            InlineKeyboardButton("ابریشم", callback_data='abrisham-isfahan'), 
            InlineKeyboardButton("اصفهان", callback_data='isfahan'), 
            InlineKeyboardButton("خوانسار", callback_data='khansar'), 
        ],
        [
            InlineKeyboardButton("داران", callback_data='daran'),
            InlineKeyboardButton("سمیرم", callback_data='semirom'), 
            InlineKeyboardButton("فلاورجان", callback_data='falavarjan'), 
            InlineKeyboardButton("کاشان", callback_data='kashan'), 
        ],
        [
            InlineKeyboardButton("گلپایگان", callback_data='golpayegan'),
            InlineKeyboardButton("نجف آباد", callback_data='najafabad'), 
        ],
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr



#######################################################################################################################################


def Ardabil(update: Update, context: CallbackContext) -> None:
    """Send message on `/Ardabil`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='ardabil-province'),        
        ],
        [
            InlineKeyboardButton("اردبیل", callback_data='ardabil'),
            InlineKeyboardButton("پارس آباد", callback_data='parsabad'), 
            InlineKeyboardButton("خلخال", callback_data='khalkhal'), 
            InlineKeyboardButton("مشکین شهر", callback_data='meshgin-shahr'), 
        ],

    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


#######################################################################################################################################



def Yazd(update: Update, context: CallbackContext) -> None:
    """Send message on `/Yazd`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='yazd-province'),        
        ],
        [
            InlineKeyboardButton("اردکان", callback_data='ardakan'),
            InlineKeyboardButton("حمیدیا", callback_data='hamidia'),         
        ],
        [
            InlineKeyboardButton("میبد", callback_data='meybod'),
            InlineKeyboardButton("یزد", callback_data='yazd'),                  
        ],

    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


###################################################################################################################################


def Azarbaijan_sharghi(update: Update, context: CallbackContext) -> None:
    """Send message on `/Azarbaijan_sharghi`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='azarbaijan-east-province'),        
        ],
        [
            InlineKeyboardButton("آذربایجان", callback_data='azarshahr'),
            InlineKeyboardButton("اهر", callback_data='ahar'), 
            InlineKeyboardButton("بناب", callback_data='bonab'), 

        ],
        [
            InlineKeyboardButton("تبریز", callback_data='tabriz'),
            InlineKeyboardButton("سرآب", callback_data='sarab'),
            InlineKeyboardButton("سهند", callback_data='sahand'), 

        ],
        [
            InlineKeyboardButton("مرند", callback_data='marand'), 
            InlineKeyboardButton("مراغه", callback_data='maragheh'),
            InlineKeyboardButton("میانه", callback_data='mianeh'),              
        ],

    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data)[1:] 
    return shahr


###################################################################################################################################


def Azarbaijan_gharbi(update: Update, context: CallbackContext) -> None:
    """Send message on `/Azarbaijan_gharbi`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [

        [
            InlineKeyboardButton("همه ی شهر ها", callback_data='azerbaijan-west-province'),        
        ],
        [
            InlineKeyboardButton("ارومیه", callback_data='urmia'),
            InlineKeyboardButton("اشنویه", callback_data='oshnavieh'), 
            InlineKeyboardButton("بوکان", callback_data='bukan'), 
            InlineKeyboardButton("پیرانشهر", callback_data='piranshahr'), 
        ],
        [
            InlineKeyboardButton("خوی", callback_data='khoy'),
            InlineKeyboardButton("سردشت", callback_data='sardasht'),
            InlineKeyboardButton("سلماس", callback_data='salmas'), 
            InlineKeyboardButton("شاهین دژ", callback_data='shahin-dej'), 
        ],
        [
            InlineKeyboardButton("ماکو", callback_data='maku'), 
            InlineKeyboardButton("مهاباد", callback_data='mahabad'),
            InlineKeyboardButton("میاندوآب", callback_data='miandoab'), 
            InlineKeyboardButton("نقده", callback_data='naqadeh'),                          
        ],

    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا شهر مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['ostan'] = str(query.data) 
    return shahr

###################################################################################################################################

def Option(update: Update, context: CallbackContext) -> None:
    """Send message on `/option`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("خودرو سواری", callback_data='car'),
            InlineKeyboardButton("فروش آپارتمان", callback_data='buy-apartment'), 
            InlineKeyboardButton("اجاره آپارتمان", callback_data='rent-apartment'), 

        ],
        [
            InlineKeyboardButton("موبایل", callback_data='mobile-phones'),
            InlineKeyboardButton("مبلمان", callback_data='sofa-armchair'),  
            InlineKeyboardButton("حیوانات", callback_data='pets-animals'),                        
        ],  
        [
            InlineKeyboardButton("وسایل شخصی", callback_data='personal-goods'),
            InlineKeyboardButton("خدمات", callback_data='services'),                        
        ],   
        [
            InlineKeyboardButton("استخدام", callback_data='jobs'),
            InlineKeyboardButton("تلوزیون", callback_data='tv-projector'),                        
        ],                     
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا دسته مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['shahr'] = str(query.data) 
    return option

 
###################################################################################################################################


def Min(update: Update, context: CallbackContext) -> None:
    """Send message on `/option`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("100,000 تومان", callback_data='100000'),
            InlineKeyboardButton("200,000 تومان", callback_data='200000'), 
            InlineKeyboardButton("500,000 تومان", callback_data='500000'),            
        ], 
        [
            InlineKeyboardButton("1,000,000 تومان", callback_data='1000000'),            
            InlineKeyboardButton("2,000,000 تومان", callback_data='2000000'),
            InlineKeyboardButton("5,000,000 تومان", callback_data='5000000'),            
        ],  
        [
            InlineKeyboardButton("10,000,000 تومان", callback_data='10000000'), 
            InlineKeyboardButton("50,000,000 تومان", callback_data='50000000'),
            InlineKeyboardButton("100,000,000 تومان", callback_data='100000000'),             
        ],                                   
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا حداقل قیمت مدنظر خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['option'] = str(query.data)     
    return min1


###################################################################################################################################


def Max(update: Update, context: CallbackContext) -> None:
    """Send message on `/option`."""
    global my_id, mydict
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("200,000 تومان", callback_data='200000'),
            InlineKeyboardButton("300,000 تومان", callback_data='300000'), 
            InlineKeyboardButton("1,000,000 تومان", callback_data='1000000'),            
        ], 
        [
            InlineKeyboardButton("2,000,000 تومان", callback_data='2000000'),            
            InlineKeyboardButton("5,000,000 تومان", callback_data='5000000'),
            InlineKeyboardButton("20,000,000 تومان", callback_data='20000000'),            
        ],  
        [
            InlineKeyboardButton("50,000,000 تومان", callback_data='50000000'), 
            InlineKeyboardButton("100,000,000 تومان", callback_data='100000000'),
            InlineKeyboardButton("1,000,000,000 تومان", callback_data='1000000000'),             
        ],                                   
    ]        

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text('لطفا حداکثر قیمت مدنظر  خود را انتخاب نمایید.', reply_markup=reply_markup)
    mydict[my_id]['min'] = int(query.data)    
    return max1


###################################################################################################################################


def Final(update: Update, context: CallbackContext) -> None:
    global my_id, mydict
    query = update.callback_query
    query.answer()
    mydict[my_id]['time'] = str(query.data)
    query.edit_message_text(text=f'موارد مورد نظر ثبت گردید.\n اگهی هایی که با درخواست شما مطابقت داشته باشد برای شما ارسال می گردد. ')

    # webscraping with beautifulsoup

    Shahr = mydict[my_id]['shahr']
    dastebandi = mydict[my_id]['option']
    mylink = f'https://divar.ir/s/{Shahr}/{dastebandi}'
    page = requests.get(mylink)
    soup = BeautifulSoup(page.text,'html.parser') 
    divtag = soup.find_all('a', {'class': 'kt-post-card kt-post-card--outlined kt-post-card--has-chat'})

    Ads = {}
    final_number = ''
    list_number = []

    for tag in divtag:
        nimlink = tag.get('href')
        al = tag.text
        # با توجه به متفاوت بودن نوع آگهی های این دو دسته بندی، شروط زیر گذاشته شده است

        if mydict[my_id]['option'] == 'car':
            al = str(al).replace('تومان', 'تومان\n')
            al = str(al).replace('توافقی','توافقی\n')
            al = str(al).replace('غیرقابل نمایش', 'غیرقابل نمایش\n')
            al = str(al).replace('جهت معاوضه','جهت معاوضه\n')
            al_list = al.split('\n')
            for c in al_list[1]:
                if c.isdigit() == True:
                   final_number += c
            if final_number == '':
                final_number = '0' 
            range_money = int(final_number) 
            final_number = ''
            if len(al_list) == 3:
                if int(mydict[my_id]['min']) <= range_money <= int(mydict[my_id]['max']):
                    if mydict[my_id]['time'] == '1 ساعت':
                        if 'فوری' in al_list[2] or 'لحظاتی' in al_list[2] or 'دقایقی' in al_list[2] or 'یک ربع' in al_list[2] or 'نیم ساعت' in al_list[2] or '۱ ساعت' in al_list[2]:
                            query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')
                    elif mydict[my_id]['time'] == '2 ساعت':
                        if 'فوری' in al_list[2] or 'لحظاتی' in al_list[2] or 'دقایقی' in al_list[2] or 'یک ربع' in al_list[2] or 'نیم ساعت' in al_list[2] or '۱ ساعت' in al_list[2] or '۲ ساعت' in al_list[2]:
                            query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')
                    elif mydict[my_id]['time'] == '3 ساعت':
                        if 'فوری' in al_list[2] or 'لحظاتی' in al_list[2] or 'دقایقی' in al_list[2] or 'یک ربع' in al_list[2] or 'نیم ساعت' in al_list[2] or '۱ ساعت' in al_list[2] or '۱ ساعت' in al_list[2] or '۳ ساعت' in al_list[2]:
                            query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')


        elif mydict[my_id]['option'] == 'jobs' or mydict[my_id]['option'] == 'services':
            al = str(al).replace('فوری', '\nفوری')
            al = str(al).replace('دقایقی', '\nدقایقی')
            al = str(al).replace('لحظاتی', '\nلحظاتی')
            al = str(al).replace('یک ربع', '\nیک ربع')
            al = str(al).replace('نیم ساعت', '\nنیم ساعت')
            al = str(al).replace('۱ ساعت', '\n۱ ساعت')
            al = str(al).replace('۲ ساعت', '\n۲ ساعت')
            al = str(al).replace('۳ ساعت', '\n۳ ساعت')
            al = str(al).replace('۴ ساعت', '\n۴ ساعت')
            al = str(al).replace('۵ ساعت', '\n۵ ساعت')
            al_list = al.split('\n')
            if mydict[my_id]['time'] == '1 ساعت':
                if 'فوری' in al_list[1] or 'لحظاتی' in al_list[1] or 'دقایقی' in al_list[1] or 'یک ربع' in al_list[1] or 'نیم ساعت' in al_list[1] or '۱ ساعت' in al_list[1]:
                    query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')
            elif mydict[my_id]['time'] == '2 ساعت':
                if 'فوری' in al_list[1] or 'لحظاتی' in al_list[1] or 'دقایقی' in al_list[1] or 'یک ربع' in al_list[1] or 'نیم ساعت' in al_list[1] or '۱ ساعت' in al_list[1] or '۲ ساعت' in al_list[1]:
                    query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')
            elif mydict[my_id]['time'] == '3 ساعت':
                if 'فوری' in al_list[1] or 'لحظاتی' in al_list[1] or 'دقایقی' in al_list[1] or 'یک ربع' in al_list[1] or 'نیم ساعت' in al_list[1] or '۱ ساعت' in al_list[1] or '۱ ساعت' in al_list[1] or '۳ ساعت' in al_list[1]:
                    query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')            


        else:
            al = tag.text
            al = str(al).replace('تومان', 'تومان\n')
            al = str(al).replace('توافقی','توافقی\n')
            al = str(al).replace('غیرقابل نمایش', 'غیرقابل نمایش\n')
            al = str(al).replace('جهت معاوضه','جهت معاوضه\n')
            al_list = al.split('\n')

            for word in al_list[0].split():
                if ',' in word:
                    for z in word:
                        if (z.isdigit() == True):
                            final_number += z
            if final_number == '':
                final_number = '0' 
            range_money = int(final_number)  #120000              
            list_number.append(al_list[0])                
            list_number.append(f'{final_number} تومان')
            list_number.append(al_list[1])
            final_number = ''
            # list_number = []  
            if int(mydict[my_id]['min']) <= range_money <= int(mydict[my_id]['max']):
                if mydict[my_id]['time'] == '1 ساعت':
                    if 'فوری' in al_list[1] or 'لحظاتی' in al_list[1] or 'دقایقی' in al_list[1] or 'یک ربع' in al_list[1] or 'نیم ساعت' in al_list[1] or '۱ ساعت' in al_list[1]:
                        query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')
                elif mydict[my_id]['time'] == '2 ساعت':
                    if 'فوری' in al_list[1] or 'لحظاتی' in al_list[1] or 'دقایقی' in al_list[1] or 'یک ربع' in al_list[1] or 'نیم ساعت' in al_list[1] or '۱ ساعت' in al_list[1] or '۲ ساعت' in al_list[1]:
                        query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')
                elif mydict[my_id]['time'] == '3 ساعت':
                    if 'فوری' in al_list[1] or 'لحظاتی' in al_list[1] or 'دقایقی' in al_list[1] or 'یک ربع' in al_list[1] or 'نیم ساعت' in al_list[1] or '۱ ساعت' in al_list[1] or '۱ ساعت' in al_list[1] or '۳ ساعت' in al_list[1]:
                        query.from_user.send_message(f'{al}\nhttps://divar.ir{nimlink}')

    query.from_user.send_message('لطفا برای شروع مجدد روی /start کیلک کنید.')
                            

###################################################################################################################################


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    TOKEN = 'Your-Telegram-Bot-Token'
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    PORT = int(os.environ.get('PORT', '8443'))
    #start
    # updater.dispatcher.add_handler(CommandHandler('start', start))  
    #help
    updater.dispatcher.add_handler(CommandHandler('help', help))     
    #Processes    
    conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                ostan: [
                    CallbackQueryHandler(Azarbaijan_sharghi, pattern='@1'),
                    CallbackQueryHandler(Azarbaijan_gharbi, pattern='@2'),
                    CallbackQueryHandler(Ardabil, pattern='@3'),
                    CallbackQueryHandler(Isfahan, pattern='@4'),
                    CallbackQueryHandler(Alborz, pattern='@5'),
                    CallbackQueryHandler(Ilam, pattern='@6'),
                    CallbackQueryHandler(Bushehr, pattern='@7'),
                    CallbackQueryHandler(Tehran, pattern='@8'),
                    CallbackQueryHandler(Chaharmahaal_va_bakhtiari, pattern='@9'),
                    CallbackQueryHandler(Khorasan_jonobi, pattern='#10'),
                    CallbackQueryHandler(Khorasan_razavi, pattern='#11'),
                    CallbackQueryHandler(Khorasan_shomali, pattern='#12'),
                    CallbackQueryHandler(Khuzestan, pattern='#13'),
                    CallbackQueryHandler(Zanjan, pattern='#14'),
                    CallbackQueryHandler(Semnan, pattern='#15'),
                    CallbackQueryHandler(Sistan_va_baluchestan, pattern='#16'),
                    CallbackQueryHandler(Fars, pattern='#17'),
                    CallbackQueryHandler(Qazvin, pattern='#18'),
                    CallbackQueryHandler(Qom, pattern='#19'),
                    CallbackQueryHandler(Kordestan, pattern='#20'),
                    CallbackQueryHandler(Kerman, pattern='!21'),
                    CallbackQueryHandler(Kermanshah, pattern='!22'),
                    CallbackQueryHandler(Kohgiluyeh_va_boyer_ahmad, pattern='!23'),
                    CallbackQueryHandler(Golestan, pattern='!24'),
                    CallbackQueryHandler(Gilan, pattern='!25'),
                    CallbackQueryHandler(Lorestan, pattern='!26'),
                    CallbackQueryHandler(Mazandaran, pattern='!27'),
                    CallbackQueryHandler(Markazi, pattern='!28'),
                    CallbackQueryHandler(Hormozgan, pattern='!29'),
                    CallbackQueryHandler(Hamadan, pattern='!30'),
                    CallbackQueryHandler(Yazd, pattern='%31'),
                ], 
                shahr:[
                    CallbackQueryHandler(Option, pattern='azarbaijan-east-province'),
                    CallbackQueryHandler(Option, pattern='azarshahr'),
                    CallbackQueryHandler(Option, pattern='ahar'),
                    CallbackQueryHandler(Option, pattern='bonab'),
                    CallbackQueryHandler(Option, pattern='tabriz'),
                    CallbackQueryHandler(Option, pattern='sarab'),
                    CallbackQueryHandler(Option, pattern='sahand'),
                    CallbackQueryHandler(Option, pattern='maragheh'),
                    CallbackQueryHandler(Option, pattern='marand'),
                    CallbackQueryHandler(Option, pattern='mianeh'),
                    CallbackQueryHandler(Option, pattern='azerbaijan-west-province'),
                    CallbackQueryHandler(Option, pattern='urmia'),
                    CallbackQueryHandler(Option, pattern='oshnavieh'),
                    CallbackQueryHandler(Option, pattern='bukan'),
                    CallbackQueryHandler(Option, pattern='piranshahr'),
                    CallbackQueryHandler(Option, pattern='khoy'),
                    CallbackQueryHandler(Option, pattern='sardasht'),
                    CallbackQueryHandler(Option, pattern='salmas'),
                    CallbackQueryHandler(Option, pattern='shahin-dej'),
                    CallbackQueryHandler(Option, pattern='maku'),
                    CallbackQueryHandler(Option, pattern='mahabad'),
                    CallbackQueryHandler(Option, pattern='miandoab'),
                    CallbackQueryHandler(Option, pattern='naqadeh'),
                    CallbackQueryHandler(Option, pattern='ardabil-province'),
                    CallbackQueryHandler(Option, pattern='ardabil'),
                    CallbackQueryHandler(Option, pattern='parsabad'),
                    CallbackQueryHandler(Option, pattern='khalkhal'),
                    CallbackQueryHandler(Option, pattern='meshgin-shahr'),
                    CallbackQueryHandler(Option, pattern='isfahan-province'),
                    CallbackQueryHandler(Option, pattern='aran-va-bidgol'),
                    CallbackQueryHandler(Option, pattern='abrisham-isfahan'),
                    CallbackQueryHandler(Option, pattern='isfahan'),
                    CallbackQueryHandler(Option, pattern='khansar'),
                    CallbackQueryHandler(Option, pattern='daran'),
                    CallbackQueryHandler(Option, pattern='semirom'),
                    CallbackQueryHandler(Option, pattern='falavarjan'),
                    CallbackQueryHandler(Option, pattern='kashan'),
                    CallbackQueryHandler(Option, pattern='golpayegan'),
                    CallbackQueryHandler(Option, pattern='najafabad'),
                    CallbackQueryHandler(Option, pattern='alborz-province'),
                    CallbackQueryHandler(Option, pattern='asara'),
                    CallbackQueryHandler(Option, pattern='eshtehard'),
                    CallbackQueryHandler(Option, pattern='tankaman'),
                    CallbackQueryHandler(Option, pattern='charbagh-alborz'),
                    CallbackQueryHandler(Option, pattern='taleqan'),
                    CallbackQueryHandler(Option, pattern='karaj'),
                    CallbackQueryHandler(Option, pattern='koohsar'),
                    CallbackQueryHandler(Option, pattern='garmdareh'),
                    CallbackQueryHandler(Option, pattern='nazarabad'),
                    CallbackQueryHandler(Option, pattern='ilam-province'),
                    CallbackQueryHandler(Option, pattern='abdanan'),
                    CallbackQueryHandler(Option, pattern='ilam'),
                    CallbackQueryHandler(Option, pattern='eyvan'),
                    CallbackQueryHandler(Option, pattern='dehloran'),
                    CallbackQueryHandler(Option, pattern='bushehr-province'),
                    CallbackQueryHandler(Option, pattern='borazjan'),
                    CallbackQueryHandler(Option, pattern='bandar-kangan'),
                    CallbackQueryHandler(Option, pattern='bandar-ganaveh'),
                    CallbackQueryHandler(Option, pattern='bushehr'),
                    CallbackQueryHandler(Option, pattern='tehran-province'),
                    CallbackQueryHandler(Option, pattern='absard'),
                    CallbackQueryHandler(Option, pattern='abali'),
                    CallbackQueryHandler(Option, pattern='arjmand'),
                    CallbackQueryHandler(Option, pattern='eslamshahr'),
                    CallbackQueryHandler(Option, pattern='baghershahr'),
                    CallbackQueryHandler(Option, pattern='pishva'),
                    CallbackQueryHandler(Option, pattern='tehran'),
                    CallbackQueryHandler(Option, pattern='javadabad'),
                    CallbackQueryHandler(Option, pattern='chahar-dangeh'),
                    CallbackQueryHandler(Option, pattern='damavand'),
                    CallbackQueryHandler(Option, pattern='shahedshahr'),
                    CallbackQueryHandler(Option, pattern='shemshak'),
                    CallbackQueryHandler(Option, pattern='sabashahr'),
                    CallbackQueryHandler(Option, pattern='safadasht-industrial-city'),
                    CallbackQueryHandler(Option, pattern='ferdosiye'),
                    CallbackQueryHandler(Option, pattern='kahrizak'),
                    CallbackQueryHandler(Option, pattern='kilan'),
                    CallbackQueryHandler(Option, pattern='golestan-baharestan'),
                    CallbackQueryHandler(Option, pattern='nasimshahr'),
                    CallbackQueryHandler(Option, pattern='vahidieh'),
                    CallbackQueryHandler(Option, pattern='chahar-mahaal-and-bakhtiari-province'),
                    CallbackQueryHandler(Option, pattern='boroujen'),
                    CallbackQueryHandler(Option, pattern='shahrekord'),
                    CallbackQueryHandler(Option, pattern='farrokhshahr'),
                    CallbackQueryHandler(Option, pattern='lordegan'),
                    CallbackQueryHandler(Option, pattern='khorasan-south-province'),
                    CallbackQueryHandler(Option, pattern='birjand'),
                    CallbackQueryHandler(Option, pattern='tabas'),
                    CallbackQueryHandler(Option, pattern='ferdows'),
                    CallbackQueryHandler(Option, pattern='ghayen'),
                    CallbackQueryHandler(Option, pattern='horasan-razavi-province'),
                    CallbackQueryHandler(Option, pattern='bardaskan'),
                    CallbackQueryHandler(Option, pattern='taybad'),
                    CallbackQueryHandler(Option, pattern='torbat-jam'),
                    CallbackQueryHandler(Option, pattern='chenaran'),
                    CallbackQueryHandler(Option, pattern='khaf'),
                    CallbackQueryHandler(Option, pattern='sabzevar'),
                    CallbackQueryHandler(Option, pattern='qasemabad-khaf'),
                    CallbackQueryHandler(Option, pattern='gonabad'),
                    CallbackQueryHandler(Option, pattern='mashhad'),
                    CallbackQueryHandler(Option, pattern='neyshabur'),
                    CallbackQueryHandler(Option, pattern='khorasan-north-province'),
                    CallbackQueryHandler(Option, pattern='ashkhaneh'),
                    CallbackQueryHandler(Option, pattern='esfarāyen'),
                    CallbackQueryHandler(Option, pattern='bojnurd'),
                    CallbackQueryHandler(Option, pattern='shirvan'),
                    CallbackQueryHandler(Option, pattern='khuzestan-province'),
                    CallbackQueryHandler(Option, pattern='abadan'),
                    CallbackQueryHandler(Option, pattern='andimeshk'),
                    CallbackQueryHandler(Option, pattern='ahvaz'),
                    CallbackQueryHandler(Option, pattern='izeh'),
                    CallbackQueryHandler(Option, pattern='bandar-imam-khomeini'),
                    CallbackQueryHandler(Option, pattern='bandar-mahshahr'),
                    CallbackQueryHandler(Option, pattern='behbahan'),
                    CallbackQueryHandler(Option, pattern='khorramshahr'),
                    CallbackQueryHandler(Option, pattern='dezful'),
                    CallbackQueryHandler(Option, pattern='ramhormoz'),
                    CallbackQueryHandler(Option, pattern='susangerd'),
                    CallbackQueryHandler(Option, pattern='shush'),
                    CallbackQueryHandler(Option, pattern='shooshtar'),
                    CallbackQueryHandler(Option, pattern='masjed-soleyman'),
                    CallbackQueryHandler(Option, pattern='zanjan-province'),
                    CallbackQueryHandler(Option, pattern='abhar'),
                    CallbackQueryHandler(Option, pattern='khorramdarreh'),
                    CallbackQueryHandler(Option, pattern='zanjan'),
                    CallbackQueryHandler(Option, pattern='qeydar'),
                    CallbackQueryHandler(Option, pattern='semnan-province'),
                    CallbackQueryHandler(Option, pattern='damghan'),
                    CallbackQueryHandler(Option, pattern='semnan'),
                    CallbackQueryHandler(Option, pattern='shahroud'),
                    CallbackQueryHandler(Option, pattern='garmsar'),
                    CallbackQueryHandler(Option, pattern='sistan-and-baluchestan-province'),
                    CallbackQueryHandler(Option, pattern='iranshahr'),
                    CallbackQueryHandler(Option, pattern='chabahar'),
                    CallbackQueryHandler(Option, pattern='zabol'),
                    CallbackQueryHandler(Option, pattern='zahedan'),
                    CallbackQueryHandler(Option, pattern='saravan'),
                    CallbackQueryHandler(Option, pattern='fars-province'),
                    CallbackQueryHandler(Option, pattern='abadeh'),
                    CallbackQueryHandler(Option, pattern='eqlid'),
                    CallbackQueryHandler(Option, pattern='jahrom'),
                    CallbackQueryHandler(Option, pattern='darab'),
                    CallbackQueryHandler(Option, pattern='shiraz'),
                    CallbackQueryHandler(Option, pattern='sadra'),
                    CallbackQueryHandler(Option, pattern='lar'),
                    CallbackQueryHandler(Option, pattern='lamerd'),
                    CallbackQueryHandler(Option, pattern='neyriz'),
                    CallbackQueryHandler(Option, pattern='qazvin-province'),
                    CallbackQueryHandler(Option, pattern='abyek'),
                    CallbackQueryHandler(Option, pattern='alvand'),
                    CallbackQueryHandler(Option, pattern='takestan'),
                    CallbackQueryHandler(Option, pattern='qazvin'),
                    CallbackQueryHandler(Option, pattern='mohammadiyeh'),
                    CallbackQueryHandler(Option, pattern='qom'),
                    CallbackQueryHandler(Option, pattern='kurdistan-province'),
                    CallbackQueryHandler(Option, pattern='baneh'),
                    CallbackQueryHandler(Option, pattern='bijar'),
                    CallbackQueryHandler(Option, pattern='saqqez'),
                    CallbackQueryHandler(Option, pattern='sanandaj'),
                    CallbackQueryHandler(Option, pattern='qorveh'),
                    CallbackQueryHandler(Option, pattern='marivan'),
                    CallbackQueryHandler(Option, pattern='kerman-province'),
                    CallbackQueryHandler(Option, pattern='bam'),
                    CallbackQueryHandler(Option, pattern='jiroft'),
                    CallbackQueryHandler(Option, pattern='rafsanjan'),
                    CallbackQueryHandler(Option, pattern='zarand'),
                    CallbackQueryHandler(Option, pattern='sirjan'),
                    CallbackQueryHandler(Option, pattern='kerman'),
                    CallbackQueryHandler(Option, pattern='kermanshah-province'),
                    CallbackQueryHandler(Option, pattern='eslamabad-gharb'),
                    CallbackQueryHandler(Option, pattern='javanrud'),
                    CallbackQueryHandler(Option, pattern='sarpol-zahab'),
                    CallbackQueryHandler(Option, pattern='sonqor'),
                    CallbackQueryHandler(Option, pattern='Kermanshah'),
                    CallbackQueryHandler(Option, pattern='kangavar'),
                    CallbackQueryHandler(Option, pattern='kohgiluyeh-and-boyer-ahmad-province'),
                    CallbackQueryHandler(Option, pattern='dogonbadan'),
                    CallbackQueryHandler(Option, pattern='dehdasht'),
                    CallbackQueryHandler(Option, pattern='yasuj'),
                    CallbackQueryHandler(Option, pattern='golestan-province'),
                    CallbackQueryHandler(Option, pattern='azadshahr-golestan'),
                    CallbackQueryHandler(Option, pattern='aq-qala'),
                    CallbackQueryHandler(Option, pattern='bandar-torkaman'),
                    CallbackQueryHandler(Option, pattern='aliabad-katul'),
                    CallbackQueryHandler(Option, pattern='kordkuy'),
                    CallbackQueryHandler(Option, pattern='kalale'),
                    CallbackQueryHandler(Option, pattern='gorgan'),
                    CallbackQueryHandler(Option, pattern='gomishan'),
                    CallbackQueryHandler(Option, pattern='gonbad-kavus'),
                    CallbackQueryHandler(Option, pattern='minoodasht'),
                    CallbackQueryHandler(Option, pattern='gilan-province'),
                    CallbackQueryHandler(Option, pattern='astara'),
                    CallbackQueryHandler(Option, pattern='astaneh-ashrafiyeh'),
                    CallbackQueryHandler(Option, pattern='amlash'),
                    CallbackQueryHandler(Option, pattern='bandar-anzali'),
                    CallbackQueryHandler(Option, pattern='talesh'),
                    CallbackQueryHandler(Option, pattern='chaboksar'),
                    CallbackQueryHandler(Option, pattern='chaf-chamkhale'),
                    CallbackQueryHandler(Option, pattern='khoshkbijar'),
                    CallbackQueryHandler(Option, pattern='rasht'),
                    CallbackQueryHandler(Option, pattern='rezvanshahr'),
                    CallbackQueryHandler(Option, pattern='zibakenar'),
                    CallbackQueryHandler(Option, pattern='rudsar'),
                    CallbackQueryHandler(Option, pattern='siahkal'),
                    CallbackQueryHandler(Option, pattern='someh-sara'),
                    CallbackQueryHandler(Option, pattern='fuman'),
                    CallbackQueryHandler(Option, pattern='kelachay'),
                    CallbackQueryHandler(Option, pattern='kiashahr'),
                    CallbackQueryHandler(Option, pattern='lahijan'),
                    CallbackQueryHandler(Option, pattern='lashtenesha'),
                    CallbackQueryHandler(Option, pattern='langarud'),
                    CallbackQueryHandler(Option, pattern='masal'),
                    CallbackQueryHandler(Option, pattern='lorestan-province'),
                    CallbackQueryHandler(Option, pattern='azna'),
                    CallbackQueryHandler(Option, pattern='aligudarz'),
                    CallbackQueryHandler(Option, pattern='borujerd'),
                    CallbackQueryHandler(Option, pattern='khorramabad'),
                    CallbackQueryHandler(Option, pattern='dorud'),
                    CallbackQueryHandler(Option, pattern='kuhdasht'),
                    CallbackQueryHandler(Option, pattern='nurabad'),
                    CallbackQueryHandler(Option, pattern='mazandaran-province'),
                    CallbackQueryHandler(Option, pattern='amol'),
                    CallbackQueryHandler(Option, pattern='amirkala'),
                    CallbackQueryHandler(Option, pattern='izadshahr'),
                    CallbackQueryHandler(Option, pattern='babol'),
                    CallbackQueryHandler(Option, pattern='babolsar'),
                    CallbackQueryHandler(Option, pattern='behshahr'),
                    CallbackQueryHandler(Option, pattern='polsefid'),
                    CallbackQueryHandler(Option, pattern='tonekabon'),
                    CallbackQueryHandler(Option, pattern='juybar'),
                    CallbackQueryHandler(Option, pattern='chalus'),
                    CallbackQueryHandler(Option, pattern='chamestan'),
                    CallbackQueryHandler(Option, pattern='ramsar'),
                    CallbackQueryHandler(Option, pattern='royan'),
                    CallbackQueryHandler(Option, pattern='sari'),
                    CallbackQueryHandler(Option, pattern='sorkhrood'),
                    CallbackQueryHandler(Option, pattern='salman-shahr'),
                    CallbackQueryHandler(Option, pattern='abbasabad-mazandaran'),
                    CallbackQueryHandler(Option, pattern='fereydunkenar'),
                    CallbackQueryHandler(Option, pattern='qaemshahr'),
                    CallbackQueryHandler(Option, pattern='kelarabad'),
                    CallbackQueryHandler(Option, pattern='kelarestan'),
                    CallbackQueryHandler(Option, pattern='mahmudabad'),
                    CallbackQueryHandler(Option, pattern='neka'),
                    CallbackQueryHandler(Option, pattern='nur'),
                    CallbackQueryHandler(Option, pattern='nowshahr'),
                    CallbackQueryHandler(Option, pattern='markazi-province'),
                    CallbackQueryHandler(Option, pattern='arak'),
                    CallbackQueryHandler(Option, pattern='khomein'),
                    CallbackQueryHandler(Option, pattern='saveh'),
                    CallbackQueryHandler(Option, pattern='mahalat'),
                    CallbackQueryHandler(Option, pattern='hormozgan-province'),
                    CallbackQueryHandler(Option, pattern='bandar-abbas'),
                    CallbackQueryHandler(Option, pattern='qeshm'),
                    CallbackQueryHandler(Option, pattern='kish'),
                    CallbackQueryHandler(Option, pattern='minab'),
                    CallbackQueryHandler(Option, pattern='hamadan-province'),
                    CallbackQueryHandler(Option, pattern='asadabad'),
                    CallbackQueryHandler(Option, pattern='tuyserkan'),
                    CallbackQueryHandler(Option, pattern='malayer'),
                    CallbackQueryHandler(Option, pattern='nahavand'),
                    CallbackQueryHandler(Option, pattern='hamedan'),
                    CallbackQueryHandler(Option, pattern='yazd-province'),
                    CallbackQueryHandler(Option, pattern='ardakan'),
                    CallbackQueryHandler(Option, pattern='hamidia'),
                    CallbackQueryHandler(Option, pattern='meybod'),
                    CallbackQueryHandler(Option, pattern='yazd')           
                ],
                option:[
                    CallbackQueryHandler(Min, pattern='car'),
                    CallbackQueryHandler(Min, pattern='buy-apartment'),
                    CallbackQueryHandler(Min, pattern='rent-apartment'),
                    CallbackQueryHandler(Min, pattern='mobile-phones'),
                    CallbackQueryHandler(Min, pattern='sofa-armchair'),
                    CallbackQueryHandler(Min, pattern='pets-animals'),
                    CallbackQueryHandler(Min, pattern='personal-goods'),
                    CallbackQueryHandler(Min, pattern='tv-projector'),
                    CallbackQueryHandler(Time, pattern='jobs'),
                    CallbackQueryHandler(Time, pattern='services'),
                ],
                min1:[
                    CallbackQueryHandler(Max, pattern='100000'),
                    CallbackQueryHandler(Max, pattern='200000'),
                    CallbackQueryHandler(Max, pattern='500000'),
                    CallbackQueryHandler(Max, pattern='1000000'),
                    CallbackQueryHandler(Max, pattern='2000000'),
                    CallbackQueryHandler(Max, pattern='5000000'),
                    CallbackQueryHandler(Max, pattern='10000000'),
                    CallbackQueryHandler(Max, pattern='50000000'),
                    CallbackQueryHandler(Max, pattern='100000000'),
                ],
                max1:[
                    CallbackQueryHandler(Time, pattern='200000'),
                    CallbackQueryHandler(Time, pattern='300000'),
                    CallbackQueryHandler(Time, pattern='1000000'),
                    CallbackQueryHandler(Time, pattern='2000000'),
                    CallbackQueryHandler(Time, pattern='5000000'),
                    CallbackQueryHandler(Time, pattern='20000000'),
                    CallbackQueryHandler(Time, pattern='50000000'),
                    CallbackQueryHandler(Time, pattern='100000000'),
                    CallbackQueryHandler(Time, pattern='1000000000'),
                ],
                time1:[
                    CallbackQueryHandler(Final, pattern='1 ساعت'),
                    CallbackQueryHandler(Final, pattern='2 ساعت'),
                    CallbackQueryHandler(Final, pattern='3 ساعت'),
                ],
            },
            fallbacks=[CommandHandler('start', start)],
        )
    dispatcher.add_handler(conv_handler)
    updater.start_webhook(listen="0.0.0.0",
                        port=PORT,
                        url_path=TOKEN,
                        webhook_url = 'Webhook-URL' + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()