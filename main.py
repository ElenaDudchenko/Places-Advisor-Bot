# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'

from telebot import TeleBot, types
import random


bot = TeleBot(token='6043370498:AAFp0bYBTF5XidWESV7oNq-p4pMdnaEO_GA', parse_mode='html') # создание бота

#библиотека с ресторанами по кухням :
italian_list = ["Amarcord \n https://yandex.ru/maps/org/amarcord/1153458764/?ll=30.359194%2C59.935669&z=16 ", " Goose Goose \n https://yandex.ru/maps/org/goose_goose/154637443849/?ll=30.322309%2C59.937017&z=16", "Cafe Italia \n https://yandex.ru/maps/org/italia/1037934720/?ll=30.374709%2C59.929844&z=15 ", "Forno Bravo Centrale \n https://yandex.ru/maps/org/forno_bravo_centrale/216676805801/?ll=30.347134%2C59.938162&z=15 ", "Betulla \n https://yandex.ru/maps/org/betulla/228633125544/reviews/?ll=30.370379%2C59.938640&z=15 ", "Il Lago del Cigni \n https://yandex.ru/maps/org/il_lago_dei_cigni/1262601259/reviews/?ll=30.234824%2C59.974049&z=13 ", "Oggi \n https://yandex.ru/maps/org/oggi_bistro/11369297500/?ll=30.288225%2C59.929272&z=14 ", "Salone pasta and bar \n https://yandex.ru/maps/org/salone_pasta_bar/205155748378/?ll=30.343563%2C59.938770&z=16", " Sea, Signora \n https://yandex.ru/maps/org/sea_signora/208812062912/?ll=30.312841%2C59.933677&z=16","Marso Polo \n https://yandex.ru/maps/org/marso_polo/91945793772/reviews/?ll=30.330217%2C59.941072&z=15", "Pizza Point \n https://yandex.ru/maps/org/pizza_point/76736948375/?ll=30.355135%2C59.941478&z=15" ]
asian_list = [" Ronnibistro \n https://yandex.ru/maps/org/ronny/154427313929/?ll=30.288288%2C59.929482&z=14 ", " Gills \n https://yandex.ru/maps/org/gills/40700006153/?ll=30.322138%2C59.932482&z=16 ", " Under the sea \n https://yandex.ru/maps/org/under_the_sea/238601318282/?ll=30.360622%2C59.936359&z=16 ", " Takeru \n https://yandex.ru/maps/org/takeru/137223417954/?ll=30.286025%2C59.939099&z=14 ", " Ikigai \n https://yandex.ru/maps/org/ikigai/15879592500/?ll=30.245214%2C60.008458&z=15", " Self Edge Japanese \n https://yandex.ru/maps/org/self_edge_japanese/25031157563/reviews/?ll=30.363344%2C59.941313&z=16 ", " Subzero \n https://yandex.ru/maps/2/saint-petersburg/chain/subzero/170455690877/filter/chain_id/170455690877/?ll=30.314302%2C59.952456&sll=30.314302%2C59.952434&z=12 ", " Chang \n https://yandex.ru/maps/org/chang/226943606537/?ll=30.320962%2C59.872331&z=16 ", "Ossu \n https://yandex.ru/maps/org/ossu_lapshichnaya/214604297005/?ll=30.358412%2C59.938707&z=15 ", " Mad \n https://yandex.ru/maps/org/mad/45809458231/?ll=30.282415%2C59.960400&z=16 ", " Duo Asia \n https://yandex.ru/maps/org/duo_asia/106066698143/reviews/?ll=30.344974%2C59.930039&z=16 ", " Wong Kar Wine \n https://yandex.ru/maps/org/wong_kar_wine/1404661375/?ll=30.339665%2C59.941804&z=16 ", " Made in China \n https://yandex.ru/maps/org/made_in_china/228924388161/?ll=30.310443%2C59.933312&z=16 ", " Ultramen \n https://yandex.ru/maps/org/ultramen/173300750840/?ll=30.333121%2C59.928062&z=14 ", " Jack and Chan \n https://yandex.ru/maps/org/jack_and_chan/1682351178/?ll=30.336736%2C59.937313&z=15 " ]
streetfood_list = [" Бюро \n https://yandex.ru/maps/2/saint-petersburg/chain/byuro_burgeryi_i_bar/203941236686/filter/chain_id/203941236686/?ll=30.313604%2C59.946701&sll=30.313605%2C59.946679&z=12 ", " Мясная Лавка \n https://yandex.ru/maps/org/myasnaya_lavka/214863173274/?ll=30.347110%2C59.938351&z=15 ", " BrosBurritos \n https://yandex.ru/maps/2/saint-petersburg/chain/bros_burritos/105506579563/filter/chain_id/105506579563/?ll=30.299187%2C59.998838&sll=30.299186%2C59.998486&z=10", " Ketch Up \n https://yandex.ru/maps/2/saint-petersburg/chain/ketch_up/236989321850/filter/chain_id/236989321850/?ll=30.303573%2C59.986895&sll=30.303573%2C59.986807&z=11 ", " Oh, my Dog \n  https://yandex.ru/maps/org/oh_my_dog_/59261217132/?ll=30.360515%2C59.927563&z=16", " Branch Garage \n hhttps://yandex.ru/maps/org/branch_garage/117179855449/?ll=30.351266%2C59.918998&z=15 " ]
russian_list = [" Русская рыбалка \n https://yandex.ru/maps/org/russkaya_rybalka/120152385330/?ll=30.233166%2C59.969290&z=13 ", " Счастье  \n hhttps://yandex.ru/maps/org/schastye/51348383135/?ll=30.343671%2C59.928932&z=16 ", " Банщики \n https://yandex.ru/maps/org/banshchiki/153291089798/menu/?ll=30.370198%2C59.930314&z=16 ", " Гусары \n https://yandex.ru/maps/org/gusary/209530054087/?ll=30.344493%2C59.933848&z=15 ", " Косуля \n https://yandex.ru/maps/org/kosulya/151449603355/?ll=30.341416%2C59.934308&z=16 ", " Шаляпин \n https://yandex.ru/maps/org/shalyapin/1154024806/menu/?ll=29.871334%2C60.171245&z=13 ", " Блок \n https://yandex.ru/maps/org/blok/1322560802/?ll=30.368788%2C59.945815&z=16 ", "  Ипполит \n https://yandex.ru/maps/org/ippolit/12554956999/?ll=30.318241%2C59.930738&z=15 "]
wine_list = [" На вина! \n https://yandex.ru/maps/org/na_vina_/182896170793/?ll=37.599756%2C55.756997&z=15 " , " Probka \n https://yandex.ru/maps/org/probka/1230088751/?ll=30.305050%2C59.948938&z=13 " , " Big Wine Freaks \n https://yandex.ru/maps/org/big_wine_freaks/70398213749/?ll=30.323136%2C59.974247&z=15 " ," Do Immigration \n https://yandex.ru/maps/org/do_immigration/1269716763/?ll=30.359310%2C59.938072&z=16 " ,"  Utopist \n https://yandex.ru/maps/org/utopist/77165214436/?ll=30.359014%2C59.937481&z=16 " ,"  Ателье Tapas & Bar \n https://yandex.ru/maps/org/tapas_bar/75537620229/?ll=30.302753%2C59.961530&z=16 " ,"  Футура-бар \n https://yandex.ru/maps/org/futura_bar/22545788073/?ll=30.317189%2C59.969629&z=15 " ," Recolte \n https://yandex.ru/maps/org/recolte/207156969625/menu/?ll=30.301538%2C59.949567&z=14 " ," Saro \n https://yandex.ru/maps/org/saro/10979543591/?ll=30.276958%2C59.964214&z=15 " ," Мечтатели \n https://yandex.ru/maps/org/mechtateli/1200023441/?ll=30.342908%2C59.936839&z=14" ]
taproom_list = [" AF Brew Taproom \n https://yandex.ru/maps/org/af_brew_taproom/37661452382/?ll=30.267493%2C59.911169&z=13" , " DolphinWolf  \n https://yandex.ru/maps/org/dolphinwolf/49685443118/?ll=30.346479%2C59.919075&z=14 " ,  " Bakunin \n https://yandex.ru/maps/org/bakunin/1258672059/?ll=30.371169%2C59.930611&z=16" , " Rockets and Bishops \n https://yandex.ru/maps/org/rockets_bishops/1416160133/?ll=30.319874%2C59.930165&z=16 " , " Карл и Фридрих \n https://yandex.ru/maps/org/karl_i_fridrikh/1227280367/?ll=30.232522%2C59.969993&z=16 " , " Brewmen \n https://yandex.ru/maps/org/brewmen_taproom/188690093440/?ll=30.314943%2C59.932564&z=15" , " Jawsspot \n https://yandex.ru/maps/org/jawsspot/1623132739/?ll=30.355502%2C59.936819&z=16" , " Пивная карта  \n https://beercard.ru/ " , " Пивная диета \n https://yandex.ru/maps/org/pivnaya_diyeta/64362707230/?ll=30.360855%2C59.939726&z=16 " , " Палата №6  \n https://yandex.ru/maps/org/palata_6/122157146206/?ll=30.353101%2C59.938675&z=15" , " Twin Peaks \n https://yandex.ru/maps/org/twin_peaks_craft_beer/193370620387/?ll=30.364270%2C59.937003&z=16" , " Dead Poet's Bar \n https://yandex.ru/maps/org/dead_poets/1180330450/?ll=30.353193%2C59.936192&z=16 " , " The Wall \n https://yandex.ru/maps/org/the_wall/68997141933/?ll=30.306798%2C59.960905&z=15 "]
fancy_list = [" Beef Zavod \n https://yandex.ru/profile/1704778653 ", " Bourgois Bohemians \n https://yandex.ru/profile/154210007652", " TarTarBar \n https://yandex.ru/profile/1736371961"," Harvest \n https://yandex.ru/profile/177439196450","Birch \n https://yandex.ru/profile/40571415653","Сад \n https://yandex.ru/profile/43738375855", " Frantsuza Bistrot \n https://yandex.ru/profile/186824743252"," Meal \n https://yandex.ru/maps/org/meal/148665613777/?ll=30.347630%2C59.943740&z=15"," Animals \n https://yandex.ru/maps/org/animals/18766618121/?ll=30.368170%2C59.938371&z=15"," Grebeshki \n https://yandex.ru/maps/org/grebeshki/14529817257/?ll=30.371693%2C59.954345&z=13"," Atlas vin Bistro \n https://yandex.ru/maps/org/atlas_vin_bistro/172287647099/?ll=30.366408%2C59.932915&z=16"," Pame \n https://yandex.ru/maps/org/pame/4894991268/?ll=30.327626%2C59.942721&z=15"]
unusual_list = [" Tiger Lily \n https://yandex.ru/maps/org/tiger_lily/5829821914/?ll=30.334948%2C59.936070&z=16 "," Co-op Garage \n https://yandex.ru/maps/org/co_op_garage/140162854447/?ll=30.322758%2C59.927041&z=15 "," Krang Pizza \n https://yandex.ru/maps/org/krang_pizza/131042138231/?ll=30.320039%2C59.929957&z=14 ","Camorra \n https://yandex.ru/maps/org/camorra/154150137900/?ll=30.358726%2C59.937991&z=16 "," Solids Billiards \n https://yandex.ru/maps/org/solids/48968794800/?ll=30.299816%2C59.961720&z=16 ","Tagliatella Caffe  \n https://yandex.ru/maps/org/tagliatella_caff_/51133035864/?ll=30.347126%2C59.933629&z=15 ","El Coipitas Bar \n https://yandex.ru/maps/org/el_copitas/72067240437/?ll=30.348624%2C59.929282&z=15 "," Лендок \n https://yandex.ru/maps/org/lendok/6802887653/?ll=30.296886%2C59.923965&z=15 "," Зеленогорск\n https://yandex.ru/maps/org/zelenogorsk/205135193967/?ll=30.345477%2C59.946825&z=15 "," 1,5 команаты \n https://yandex.ru/maps/org/poltory_komnaty/1523954752/?ll=30.355096%2C59.940114&z=15 "," Aphoteke Bar \n https://yandex.ru/maps/org/apotheke_bar/1592603472/?ll=30.328750%2C59.931594&z=16 "]
coffee_list = [" Sibaristica \n https://yandex.ru/maps/org/sibaristika/10847347823/?ll=30.283861%2C59.910208&z=16 ", " Verle Garden \n https://yandex.ru/maps/org/verl_/1688651543/menu/?ll=30.314458%2C59.963230&z=16 "," ТЧК \n https://yandex.ru/maps/org/tchk/1940155326/?ll=30.316434%2C59.959196&z=14 "," Coffee 22 \n https://yandex.ru/maps/org/coffee_22/102145545931/?ll=30.320029%2C59.931224&z=15",  "Coffee 3 \n https://yandex.ru/maps/org/coffee_3/181064478603/?ll=30.316842%2C59.969651&z=15 ","Больше Кофе  \n https://yandex.ru/maps/org/bolshe_kofe/1180828754/?ll=30.320602%2C59.954478&z=14 ","Civil  \n https://yandex.ru/maps/org/civil/129408254866/menu/?ll=30.321878%2C59.938482&z=16 "," Surf Coffee \n https://yandex.ru/maps/2/saint-petersburg/chain/surf_coffee/200959754479/filter/chain_id/200959754479/?ll=30.397567%2C59.992282&sll=30.397567%2C59.991930&z=10 "," Gran \n https://yandex.ru/maps/org/gr_n/154517672772/?ll=30.325004%2C59.926684&z=16 "," Kos \n https://yandex.ru/maps/org/kos_place/128720879685/menu/?ll=30.330909%2C59.926003&z=14 ","Характер кофе  \n  https://yandex.ru/maps/org/kharakter_kofe/96233915733/reviews/?ll=30.318746%2C59.922894&z=15","Mad Espresso Team  \n https://yandex.ru/maps/org/mad_espresso_team/1265503173/?ll=30.372639%2C59.930193&z=15 ","Espresso Bike  \n  https://yandex.ru/maps/org/espresso_bike/128658215202/?ll=30.321043%2C59.932378&z=16","Пенка  \n https://yandex.ru/maps/org/penka/110277893736/?ll=30.360892%2C59.938257&z=16 ","Щегол  \n https://yandex.ru/maps/org/shchegol_kofe/107955895841/?ll=30.363514%2C59.941901&z=15 " ]
aii_in_1_list = [" Василеостровский рынок \n https://yandex.ru/maps/org/vasileostrovskiy_rynok/230888383637/inside/?ll=30.285362%2C59.939343&z=16 ", " Московский рынок \n https://yandex.ru/maps/org/moskovskiy_rynok/137305570564/?ll=30.323746%2C59.879168&z=16", " City Food \n https://yandex.ru/maps/org/city_food/81397936069/reviews/?ll=30.300884%2C60.005378&z=16", " Балаган \n https://yandex.ru/maps/org/balagan/147021361953/?ll=30.298313%2C59.961532&z=14", " Фуд Парк \n https://yandex.ru/maps/org/fud_park_merkuriy/148622169203/?ll=30.205789%2C59.990899&z=16", " Гондза Бондза \n https://gondzabondza.ru/", " Севкабель Порт \n https://sevcableport.ru/ru/food", " Фабрика \n https://foodhall-fabrika.ru/restaurant/", " Vokzal 1853 \n https://vokzal1853.ru/places/", " Eat Market \n https://eatmarket.ru/ "]


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Итальянская 🍕")
    btn2 = types.KeyboardButton("Азиатская 🍣")
    btn3 = types.KeyboardButton("Стритфуд 🍔")
    btn4 = types.KeyboardButton("Русская 🥟")
    btn5 = types.KeyboardButton("Вино 🍷")
    btn6 = types.KeyboardButton("Пиво 🍺")
    btn7 = types.KeyboardButton(" Особый случай 🥂")
    btn8 = types.KeyboardButton("Что то необычное 🌶")
    btn9 = types.KeyboardButton("Кофе ☕️")
    btn10 = types.KeyboardButton("100 в 1👀")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Выбирай, куда мы сегодня пойдем 😉".format(message.from_user), reply_markup=markup)
    bot.send_video(message.chat.id, 'https://tenor.com/ru/view/cat-ringing-eating-restaurants-near-me-gif-9157660', None, 'Text')

# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Итальянская 🍕"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(italian_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующий Итальянский 🍕")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующий Итальянский 🍕"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(italian_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")

    elif(message.text == "Азиатская 🍣"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(asian_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующий Азиатский 🍣")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующий Азиатский 🍣"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(asian_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")

    elif(message.text == "Стритфуд 🍔"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(streetfood_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующий Стритфуд 🍔")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующий Стритфуд 🍔"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(streetfood_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")
  
  
    elif(message.text == "Русская 🥟"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(russian_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующий Русский 🥟")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующий Русский 🥟"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(russian_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")
  
  
    elif(message.text == "Вино 🍷"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(wine_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующее Вино 🍷")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующее Вино 🍷"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(wine_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")

    elif(message.text == "Пиво 🍺"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(taproom_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующее Пиво 🍺")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующее Пиво 🍺"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(taproom_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")

    elif(message.text == "Особый случай 🥂"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(fancy_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующий Особый случай 🥂")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующий Особый случай 🥂"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(fancy_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")


    elif(message.text == "Что то необычное 🌶"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(unusual_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующее Что то необычное 🌶")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующее Что то необычное 🌶"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(unusual_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")


    elif(message.text == "Кофе ☕️"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(coffee_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующий Кофе ☕️")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующий Кофе ☕️"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(coffee_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")

    elif(message.text == "100 в 1👀"):
     bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(aii_in_1_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton(" То, что нужно! Спасибо🤩")
     btn2 = types.KeyboardButton("Следующий 100 в 1👀")
     btn3 = types.KeyboardButton("Выбрать другую категорию 🧐")
     markup.add(btn1, btn2, btn3)
     bot.send_message(message.chat.id,text="Ну что, идем ?☺️", reply_markup=markup)

    elif(message.text == "Следующий 100 в 1👀"):
      bot.send_message(message.chat.id,"Сегодня идем в:\n\n{0}".format(random.choice(aii_in_1_list)))
      bot.send_message(message.chat.id,text="Может быть сюда? 🐱")

    elif(message.text == "То, что нужно! Спасибо🤩"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id,text="Welcome! Рад помочь 🐶", reply_markup=markup)
        bot.send_video(message.chat.id,'https://tenor.com/ru/view/happy-christmas-eve-santa-is-gif-24252291', None, 'Text')
    
    elif (message.text == "Выбрать другую категорию 🧐"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Итальянская 🍕")
        btn2 = types.KeyboardButton("Азиатская 🍣")
        btn3 = types.KeyboardButton("Стритфуд 🍔")
        btn4 = types.KeyboardButton("Русская 🥟")
        btn5 = types.KeyboardButton("Вино 🍷")
        btn6 = types.KeyboardButton("Пиво 🍺")
        btn7 = types.KeyboardButton(" Особый случай 🥂")
        btn8 = types.KeyboardButton("Что то необычное 🌶")
        btn9 = types.KeyboardButton("Кофе ☕️")
        btn10 = types.KeyboardButton("100 в 1👀")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню😉", reply_markup=markup)
    
    else:
        bot.send_message(message.chat.id, text="Не понимаю тебя😟")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
