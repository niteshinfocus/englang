import random

my_array = [
    {
        'english':"A traveler approached a holy river and was advised by a wise sage to practice Ahimsa (non-violence) towards all living beings. From that day forward, the traveler vowed to treat every creature with kindness",
        'hindi':"एक यात्री एक पवित्र नदी के पास पहुंचा और उसे एक बुद्धिमान ऋषि ने सभी जीवित प्राणियों के प्रति अहिंसा (अहिंसा) का अभ्यास करने की सलाह दी। उस दिन के बाद से, यात्री ने सभी प्राणियों के साथ दया का व्यवहार करने की कसम खाई।"
    },
    {
        'english':"In a marketplace, a merchant learned the importance of non-stealing when he realized that his dishonest practices were causing harm to others.",
        'hindi':"एक बाज़ार में, एक व्यापारी ने गैर-चोरी के महत्व को सीखा जब उसने महसूस किया कि उसकी बेईमानी दूसरों को नुकसान पहुँचा रही थी।"
    },
    {
        'english':"A young student sought guidance from a spiritual guru, who taught him the principle of Satya (truthfulness). The student embraced this teaching and became known for his honesty.",
        'hindi':"एक युवा छात्र ने एक आध्यात्मिक गुरु से मार्गदर्शन मांगा, जिन्होंने उसे सत्य (सच्चाई) का सिद्धांत सिखाया। छात्र ने इस शिक्षण को अपनाया और अपनी ईमानदारी के लिए जाना जाने लगा।"
    },
    {
        'english':"In a village, a wise elder preached the concept of Vasudhaiva Kutumbakam (the world is one family). The villagers embraced this teaching and worked towards unity and harmony, transcending barriers of caste.",
        'hindi':"एक गाँव में, एक बुद्धिमान बुजुर्ग ने वसुधैव कुटुम्बकम (विश्व एक परिवार है) की अवधारणा का प्रचार किया। ग्रामीणों ने इस शिक्षा को अपनाया और जाति की बाधाओं को पार करते हुए एकता और सद्भाव की दिशा में काम किया।"
    },
    {
        'english':"A young woman performs her duties without attachment to the results (karma-yoga), she found inner peace and transformed her challenges into opportunities for growth.",
        'hindi':"एक युवा महिला ने परिणाम (कर्म-योग) के प्रति आसक्ति के बिना अपना काम किया, उसने आंतरिक शांति पाई और अपनी चुनौतियों को विकास के अवसरों में बदल दिया।"
    },
    {
        'english':"I woke up early and had a healthy breakfast before heading to work.",
        'hindi':"मैं जल्दी उठा और काम पर जाने से पहले स्वस्थ नाश्ता किया।"
    },
    {
        'english':"The children played happily in the park, laughing and running around.",
        'hindi':"बच्चे पार्क में खुशी-खुशी खेलते, हंसते-हंसते इधर-उधर भागते।"
    },
    {
        'english':"She studied diligently for her upcoming exams to ensure good grades.",
        'hindi':"उसने अच्छे ग्रेड सुनिश्चित करने के लिए अपनी आगामी परीक्षाओं के लिए लगन से अध्ययन किया।"
    },
    {
        'english':"We enjoyed a beautiful sunset at the beach, feeling the gentle breeze on our faces.",
        'hindi':"हमने अपने चेहरे पर कोमल हवा को महसूस करते हुए समुद्र तट पर एक सुंदर सूर्यास्त का आनंद लिया"
    },
    {
        'english':"The teacher explained the lesson clearly, making it easy for the students to understand.",
        'hindi':"शिक्षक ने पाठ को स्पष्ट रूप से समझाया, जिससे छात्रों को समझने में आसानी हुई।"
    },
    {
        'english':"They organized a surprise party for their friend's birthday and it turned out to be a great success.",
        'hindi':"उन्होंने अपने दोस्त के जन्मदिन के लिए एक सरप्राइज पार्टी का आयोजन किया और यह एक बड़ी सफलता रही।"
    },
    {
        'english':"My grandmother shared fascinating stories about her childhood, leaving us amazed.",
        'hindi':"मेरी दादी ने अपने बचपन के बारे में आकर्षक कहानियाँ साझा कीं, जिससे हम चकित रह गए।"
    },
    {
        'english':"Ram found a lost wallet on the street and returned it to its owner, who was incredibly grateful and rewarded him for his honesty.",
        'hindi':"राम को सड़क पर एक खोया हुआ बटुआ मिला और उसने उसे उसके मालिक को लौटा दिया, जो अविश्वसनीय रूप से आभारी था और उसे उसकी ईमानदारी के लिए पुरस्कृत किया"
    },
    {
        'english':"Rahul, a young boy, overcame his fear of swimming by taking swimming lessons. With practice and determination, he eventually learned how to swim and enjoyed his time in the water.",
        'hindi':"राहुल, एक युवा लड़के ने तैराकी सीख कर अपने तैराकी के डर पर काबू पाया। अभ्यास और दृढ़ संकल्प के साथ, उसने आखिरकार तैरना सीख लिया और पानी में अपने समय का आनंद लिया।"
    },
    {
        'english':"I wake up early every morning and have a cup of coffee.",
        'hindi':"मैं रोज सुबह जल्दी उठता हूं और एक कप कॉफी पीता हूं।"
    },
    {
        'english':"Sita loves playing the guitar and sings beautifully.",
        'hindi':"सीता को गिटार बजाना बहुत पसंद है और वह सुंदर गाती है।"
    },
    {
        'english':"Children visited the beach and played with sand and water",
        'hindi':"बच्चे समुद्र तट पर गए और रेत और पानी से खेले"
    },
    {
        'english':"We often go for walks in the park on sunny days with our dogs",
        'hindi':"हम अक्सर अपने कुत्तों के साथ धूप के दिनों में पार्क में टहलने जाते हैं"
    },
    {
        'english':"He likes to eat dosa on weekends but he hates western junk food.",
        'hindi':"उन्हें वीकेंड पर डोसा खाना पसंद है लेकिन उन्हें पश्चिमी जंक फूड से नफरत है।"
    },
    {
        'english':"Every morning, I wake up early, do exercise, meditation and drink a fresh cup of milk.",
        'hindi':"हर सुबह मैं जल्दी उठता हूं, व्यायाम करता हूं, ध्यान करता हूं और एक ताजा कप दूध पीता हूं"
    },
    {
        'english':"My sister is studying in college and We play football every weekend",
        'hindi':" मेरी बहन कॉलेज में पढ़ रही है और हम हर वीकेंड फुटबॉल खेलते हैं"
    },
    {
        'english':"They are watching a movie but I like to read books.",
        'hindi':"वे एक फिल्म देख रहे हैं लेकिन मुझे किताबें पढ़ना पसंद है।"
    },
    {
        'english':"A group of villagers, torn by caste divisions, learned about the friendship of 'Sri Ram' and 'Kevat' ",
        'hindi':"जातिगत बंटवारे से बंटे ग्रामीणों के समूह ने जानी 'श्री राम' और 'केवट' की दोस्ती के बारे में"
    },
    {
        'english':"A group of businessman were taking lessons from Bhagwat Gita to run their business wisely.",
        'hindi':"व्यवसायियों का एक समूह भगवत गीता से अपना व्यवसाय बुद्धिमानी से चलाने के लिए शिक्षा ले रहा था"
    },
    {
        'english':"In my family, we cook together on Sundays. We gather in the kitchen and prepare delicious meals.",
        'hindi':" मेरे परिवार में, हम रविवार को एक साथ खाना बनाते हैं। हम रसोई में इकट्ठा होते हैं और स्वादिष्ट भोजन तैयार करते हैं "
    },
]

max = len(my_array)
randNo = random.randint(0, max-1)
random_script = my_array[randNo]
engScript = random_script['english']
hinScript = random_script['hindi']

