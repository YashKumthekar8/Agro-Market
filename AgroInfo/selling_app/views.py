from django.shortcuts import render
from .models import Plant,Location,User,Fertilizer
from django.contrib.auth.decorators import login_required


individual_sellers_link = {
    'VEGGOVILLA FRUITS AND VEGETABLES': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d121056.14367996114!2d73.78848046052586!3d18.528699237707613!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2b8c87c900001%3A0xeaee1a777de6dde7!2sVEGGOVILLA%20FRUITS%20AND%20VEGETABLES!5e0!3m2!1sen!2sin!4v1634123981546!5m2!1sen!2sin',
    'Gajanan Fruit Agency': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30551.81127037603!2d74.55060473955076!3d16.8275264!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc118ed6ae387cd%3A0x4b7345e2917c767c!2sGajanan%20Fruit%20Agency!5e0!3m2!1sen!2sin!4v1634124522630!5m2!1sen!2sin',
    'Vegetable & fruit': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d59991.086111801094!2d73.73658524681845!3d19.98991859497926!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bddedc8eba47521%3A0xda2635dbee7883b3!2sVegetable%20%26%20fruit!5e0!3m2!1sen!2sin!4v1634124670488!5m2!1sen!2sin',
    'Shree Bhulai Prajapati Vegetable & Fruit Company': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d59991.086111801094!2d73.73658524681845!3d19.98991859497926!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bddea4d3a232f45%3A0xa8ddcfe9b50308de!2sShree%20Bhulai%20Prajapati%20Vegetable%20%26%20Fruit%20Company!5e0!3m2!1sen!2sin!4v1634124780322!5m2!1sen!2sin',
    'Vegetable Market Yard': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30162.705121341463!2d74.72996111057522!3d19.092816268936417!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdcb05b9b9d65c9%3A0xecd935aa9e557123!2sVegetable%20Market%20Yard!5e0!3m2!1sen!2sin!4v1634124909086!5m2!1sen!2sin',
    'Sangola Agro Pvt Ltd': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30415.349738685487!2d75.90178545919382!3d17.654008373030393!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc5da7c15555547%3A0x8e8b29e7f00d64f3!2sSangola%20Agro%20Pvt%20Ltd!5e0!3m2!1sen!2sin!4v1634124987492!5m2!1sen!2sin',
    'Jalgaon Vegmart': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d29798.59799088098!2d75.53977851256593!3d20.99966100049746!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd90fa7bfec83ff%3A0xd887dfe1f9947e77!2sJalgaon%20Vegmart!5e0!3m2!1sen!2sin!4v1634125120771!5m2!1sen!2sin',
    'Sharda vegetables and fruit shop': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d60101.97697807996!2d72.72633447910152!3d19.696713799999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be71dce9d1ea0f9%3A0x312650e195bbf50b!2sSharda%20vegetables%20and%20fruit%20shop!5e0!3m2!1sen!2sin!4v1634125326495!5m2!1sen!2sin',
    'Vegetable Market': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30524.825010931458!2d73.31172540859521!3d16.994061148505953!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bea0d232cda1753%3A0x8df615db2c7548e3!2sVegetable%20Market!5e0!3m2!1sen!2sin!4v1634125418978!5m2!1sen!2sin',
    'Shubham Sabji Merchant & Fruit Center': 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d59558.3117063538!2d79.0380906!3d21.0968334!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd4c6f2ab25058b%3A0xaf9c9edbb41e7ec!2sShubham%20Sabji%20Merchant%20%26%20Fruit%20Center!5e0!3m2!1sen!2sin!4v1634125569751!5m2!1sen!2sin',
    'Khan Vegetable Seller': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d59558.314589014735!2d79.03791889613231!3d21.096826212022293!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd4c0c0bb8b1a49%3A0xbebf415b6ef9746b!2sKhan%20Vegetable%20Seller!5e0!3m2!1sen!2sin!4v1634125656358!5m2!1sen!2sin',
    'Salim Bagwan Vegetables and Fruits Shop': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30369.515632986175!2d73.64146053955079!3d17.923315400000025!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc265828d56274d%3A0xba8b030c12eb2f7e!2sSalim%20Bagwan%20Vegetables%20and%20Fruits%20Shop!5e0!3m2!1sen!2sin!4v1634125728888!5m2!1sen!2sin',
    'Vegetable wholesale market': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d121617.57195547066!2d73.3230811582031!3d17.71874710000001!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be9dfb83f477cfd%3A0x5b847496636796d9!2z4KSb4KSk4KWN4KSw4KSq4KSk4KWAIOCkuOCkguCkreCkvuCknOClgCDgpK7gpLngpL7gpLDgpL7gpJwg4KSt4KS-4KSc4KWAIOCkruCkguCkoeCkiA!5e0!3m2!1sen!2sin!4v1634125869078!5m2!1sen!2sin',
    'Shetkari Bhandar - Farmer To Consumer Shop': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d59555.072802920266!2d79.02055857910159!3d21.1049082!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd4bf9af9320d39%3A0x45d9b09884721e82!2sShetkari%20Bhandar%20-%20Farmer%20To%20Consumer%20Shop!5e0!3m2!1sen!2sin!4v1634126801428!5m2!1sen!2sin',
    'Shree Krishna Vegetables and fruits': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d121058.36515107859!2d73.80123766047596!3d18.525561839587592!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2b96b317dadd3%3A0xbe44bbb8da5ec26f!2sShree%20Krishna%20Vegetables%20and%20fruits!5e0!3m2!1sen!2sin!4v1634126769670!5m2!1sen!2sin',
    'Ichhamani Fresh Vegetable And Fruits': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d60006.601669485855!2d73.79119107910155!3d19.949143000000003!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdd954f1a4b9e2d%3A0xab525ba3bdbb932b!2sIchhamani%20Fresh%20Vegetable%20And%20Fruits!5e0!3m2!1sen!2sin!4v1634126863032!5m2!1sen!2sin',
    'Shree Mahalaxmi Bhaji Center': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d122105.70968052234!2d73.24483675820314!3d16.9842168!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bea0d1b71bd003b%3A0x865ba6e6ea9a166f!2sShree%20Mahalaxmi%20Bhaji%20Center!5e0!3m2!1sen!2sin!4v1634126952344!5m2!1sen!2sin',
    'Quality Fresh Fruits & Vegetables': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d59597.69462245393!2d75.56097925115816!3d20.998412102097287!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd90fb74be228bf%3A0x176ff6c4a5c572bc!2sQuality%20Fresh%20Fruits%20%26%20Vegetables!5e0!3m2!1sen!2sin!4v1634127013401!5m2!1sen!2sin',
    
    'The Trillion Roses Pune': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3782.211974177385!2d73.80982185046359!3d18.564479787321506!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bf9d28cbf337%3A0xd6982124d439a393!2sThe%20Trillion%20Roses%20Pune!5e0!3m2!1sen!2sin!4v1634469871413!5m2!1sen!2sin",
    'Orchid Flora Nursery': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.8348753547525!2d73.8225312504625!3d18.49113728736447!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2951719751c17%3A0x13c4b27430e72a9c!2sOrchid%20Flora%20Nursery!5e0!3m2!1sen!2sin!4v1634469898947!5m2!1sen!2sin",
    "Shamun's Flowers": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.4005080791208!2d73.87668255046282!3d18.51079478735291!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c04843188c8f%3A0x76ef7b33e313d1c5!2s93%2C%20MG%20Road%2C%20opposite%20ICICI%20bank%2C%20Camp%2C%20Pune%2C%20Maharashtra%20411001!5e0!3m2!1sen!2sin!4v1634469919479!5m2!1sen!2sin",
    'Flower Link': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3818.280750172436!2d74.57399215043911!3d16.862000888338553!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc1191c1a2765df%3A0xf0f8a50579560f9e!2sFlower%20Link!5e0!3m2!1sen!2sin!4v1634469952050!5m2!1sen!2sin",
    'Japanese Florist': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7636.79134691392!2d74.56958073488768!3d16.8563104!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc118696b3f373d%3A0x5e947febb3245545!2sJapanese%20Florist!5e0!3m2!1sen!2sin!4v1634470013653!5m2!1sen!2sin",
    'Ferns N Petals : Florist': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3750.2846870323256!2d73.83325190048532!3d19.95452633652419!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bddbf87021a532b%3A0x18bb51aa11e594a!2sFerns%20N%20Petals%20%3A%20Florist!5e0!3m2!1sen!2sin!4v1634470047528!5m2!1sen!2sin",
    'Dandvate Flowers': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3749.825536702555!2d73.78519895048555!3d19.973837986513285!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bddeb23bf39a9c1%3A0xc0fee76d68b758cd!2sDandvate%20Flowers!5e0!3m2!1sen!2sin!4v1634470072673!5m2!1sen!2sin",
    'Shreenivas Flower Shop': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14997.777984953906!2d73.75311817144656!3d19.98985078406787!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bddeb7057c7cfdb%3A0xb59ae1e23f0f24c7!2sShreenivas%20Flower%20Shop!5e0!3m2!1sen!2sin!4v1634470100113!5m2!1sen!2sin",
    'Ambika Florist': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3770.1048128941434!2d74.73220185047185!3d19.103057287008966!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdcb07d42a52be1%3A0x81441994a9caeb56!2sAmbika%20Florist!5e0!3m2!1sen!2sin!4v1634470134786!5m2!1sen!2sin",
    'Just Flowers': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3769.8335618274373!2d74.73069135047199!3d19.114956187002146!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdcba874a5f8a4b%3A0xe683c2326f826333!2sJust%20Flowers!5e0!3m2!1sen!2sin!4v1634470175517!5m2!1sen!2sin",
    'Vinayak flower Shop': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3801.286341332802!2d75.91238805045072!3d17.683928387842183!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc5da8ed453c901%3A0xca6199d2fc037053!2sVinayak%20flower%20Shop!5e0!3m2!1sen!2sin!4v1634470197319!5m2!1sen!2sin",
    'Shrinivas Flower Stall': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3801.411413898211!2d75.91282145045055!3d17.678014637845667!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc5da6275905637%3A0xb0bcd128feb4b512!2sShrinivas%20Flower%20Stall!5e0!3m2!1sen!2sin!4v1634470226298!5m2!1sen!2sin",
    'Ferns N Petals : Flower Shop': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3724.7541202850007!2d75.55698575050262!3d21.002491085943927!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd90fa2c30def17%3A0x597e2d9597713709!2sFerns%20N%20Petals%20%3A%20Flower%20Shop%20in%20Jillha%20Peth%2C%20Jalgaon!5e0!3m2!1sen!2sin!4v1634108797608!5m2!1sen!2sin",
    'Jay Ambe Flowers Decorators': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3724.4772831269324!2d75.56239855050279!3d21.013580435937893!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd90fa49ddd8439%3A0xfc44b52d0233bf0d!2sJay%20Ambe%20Flowers%20Decorators!5e0!3m2!1sen!2sin!4v1634470257622!5m2!1sen!2sin",
    'Pardeshi Flower Stall': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3756.341056707591!2d72.76846065048122!3d19.69809868666894!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be71ce84ffba283%3A0x78c87ca27791fb12!2sPardeshi%20Flower%20Stall!5e0!3m2!1sen!2sin!4v1634470281125!5m2!1sen!2sin",
    'Vrukshavalli Nursery & Garden': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30524.58905828272!2d73.32401090859649!3d16.995510248449573!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bea0d169ad35e65%3A0xf0455b0444fc8398!2sVrukshavalli%20Nursery%20%26%20Garden%20Store!5e0!3m2!1sen!2sin!4v1634470320925!5m2!1sen!2sin",
    'Mahalaxmi Nursery Harchiri': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3816.7087763429718!2d73.44282595044024!3d16.93965168829118!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bea757386eb8ff3%3A0xd02407086216d15b!2sMahalaxmi%20Nursery%20Harchiri!5e0!3m2!1sen!2sin!4v1634470360788!5m2!1sen!2sin",
    'Riya Flowers': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3721.2888337268855!2d79.06417025050493!3d21.14090078586871!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd4c08ba6ad4e9b%3A0xfc2c0678701528ba!2sRiya%20Flowers!5e0!3m2!1sen!2sin!4v1634470404186!5m2!1sen!2sin",
    'Mahajan Florist': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3721.3027974448783!2d79.05839515050488!3d21.140344785869054!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bd4c060e185233d%3A0x8fb1386f9d98a788!2sMahajan%20Florist!5e0!3m2!1sen!2sin!4v1634470447305!5m2!1sen!2sin",
    'RAJ flower shop': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3796.1321596006983!2d73.65486475045417!3d17.925988787697907!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2651d898053e1%3A0x609449369d4f5adf!2sRAJ%20flower%20shop!5e0!3m2!1sen!2sin!4v1634470526670!5m2!1sen!2sin",
    "Shamun's Flowers": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.400090235845!2d73.87669565046279!3d18.510813687352893!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2c048ea9ed0b3%3A0xfd9226c41421369b!2sShamun&#39;s%20Flowers!5e0!3m2!1sen!2sin!4v1634470562266!5m2!1sen!2sin",
    'Florist': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3783.04131007348!2d73.83632702145815!3d18.527035262153834!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bc2bf78d0798b11%3A0xaad19fa97f8bd6df!2sFlorist!5e0!3m2!1sen!2sin!4v1634470609180!5m2!1sen!2sin"
}






individual_sellers = {
    'VEGGOVILLA FRUITS AND VEGETABLES': [18.586835133692674, 73.78097225292152],
    'Gajanan Fruit Agency': [16.8275264, 74.5506047],
    'Vegetable & fruit': [19.9899186, 73.7365852],
    'Shree Bhulai Prajapati Vegetable & Fruit Company': [19.9899186, 73.7365852],
    'Vegetable Market Yard': [19.0928163, 74.7299611],
    'Sangola Agro Pvt Ltd': [17.6540084, 75.9017855],
    'Jalgaon Vegmart': [21.01065505666256, 75.55123521248589],
    'Sharda vegetables and fruit shop': [19.6967138, 72.7263345],
    'Vegetable Market': [16.9940611,	73.3117254],
    'Shubham Sabji Merchant & Fruit Center': [21.0968334, 79.0380906],
    'Khan Vegetable Seller': [21.0968262, 79.0379189],
    'Salim Bagwan Vegetables and Fruits Shop': [17.9233154,	73.6414605],
    'Vegetable wholesale market': [17.7187471, 73.3230812],
    'Shetkari Bhandar - Farmer To Consumer Shop': [21.0968334, 79.0380906],
    'Shree Krishna Vegetables and fruits': [18.5286992,	73.7884805],
    'Ichhamani Fresh Vegetable And Fruits': [19.94940519790273, 73.8261456241046],
    'Shree Mahalaxmi Bhaji Center': [16.9940611, 73.3117254],
    'Quality Fresh Fruits & Vegetables': [20.999661, 75.5397785],
    
    'The Trillion Roses Pune': [18.564713710306435, 73.81196225292122],
    'Orchid Flora Nursery': [18.5286992, 73.7884805],
    "Shamun's Flowers": [18.511068031324335, 73.87886823942995],
    'Flower Link': [16.8275264,	74.5506047],
    'Japanese Florist': [16.8275264	,74.5506047],
    'Ferns N Petals' : [20.01043542864037, 73.77197467263963],
    'Dandvate Flowers': [19.984952,	73.7441793],
    'Shreenivas Flower Shop': [19.990172775010006, 73.76189421091456],
    'Ambika Florist': [19.0997288,	74.7102217],
    'Just Flowers': [20.002394864728373, 73.77350791247024],
    'Vinayak flower Shop': [17.6596127,	75.8848142],
    'Shrinivas Flower Stall': [17.8596127,	75.8848142],
    'Ferns N Petals' : [19.957651233687926, 73.83413465998098],
    'Jay Ambe Flowers Decorators': [21.0001783,	75.5607392] ,
    'Pardeshi Flower Stall': [19.545743, 72.3476059],
    'Vrukshavalli Nursery & Garden': [16.9244626,	73.2917823],
    'Mahalaxmi Nursery Harchiri': [16.939831350636783, 73.4450053868601],
    'Riya Flowers': [21.1324634, 79.0605047],
    'Mahajan Florist': [21.4324634, 79.5605047],
    'RAJ flower shop': [17.9259888,	73.6548648],
    "Shamun's Flowers": [18.5108137, 73.318587],
    'Florist': [18.5108137,	74.318587]
}


sellers_products_based = {
    'strawberry': {1: 'Salim Bagwan Vegetables and Fruits Shop'},
    'blackberry': {1: 'Salim Bagwan Vegetables and Fruits Shop'},
    'grape': {1: 'Gajanan Fruit Agency', 2: 'Vegetable & fruit', 3: 'Sangola Agro Pvt Ltd'},
    'orange': {1: 'Shubham Sabji Merchant & Fruit Center', 2: 'Shetkari Bhandar - Farmer To Consumer Shop'},
    'mango': {1:'VEGGOVILLA FRUITS AND VEGETABLES' , 2: 'Sharda vegetables and fruit shop', 3: 'Vegetable Market'},	  	
    'banana': {1: 'Shree Bhulai Prajapati Vegetable & Fruit Company', 2: 'Jalgaon Vegmart', 3: 'Vegetable Market'},

    'potato': {1: 'Jalgaon Vegmart', 2: 'Vegetable wholesale market'},
    'tomato': {1: 'Vegetable Market', 2: 'Salim Bagwan Vegetables and Fruits Shop', 3: 'Vegetable wholesale market'},
    'spinach': {1: 'Sharda vegetables and fruit shop', 2: 'Shree Krishna Vegetables and fruits' , 3: 'Shree Mahalaxmi Bhaji Center'},
    'onion': {1: 'VEGGOVILLA FRUITS AND VEGETABLES', 2: 'Gajanan Fruit Agency', 3: 'Jalgaon Vegmart'},
    'cabbage': {1: 'Vegetable & fruit', 2: 'Jalgaon Vegmart', 3: 'Shree Krishna Vegetables and fruits'},
    'beans': {1: 'Shetkari Bhandar - Farmer To Consumer Shop', 2: 'Ichhamani Fresh Vegetable And Fruits'},
    'chili': {1: 'Vegetable Market Yard', 2: 'Sangola Agro Pvt Ltd'},	
    'peas': {1: 'Sangola Agro Pvt Ltd', 2: 'Sharda vegetables and fruit shop', 3: 'Shree Mahalaxmi Bhaji Center'},

    'lotus': {1: 'The Trillion Roses Pune', 2: 'Just Flowers'},
    'Marigold': {1: 'Jay Ambe Flowers Decorators', 2: 'Vrukshavalli Nursery & Garden'},
    'Hibiscus': {1: 'Ferns N Petals', 2: 'Vinayak flower Shop'},
    'jasmine': {1: 'Orchid Flora Nursery', 2: 'Japanese Florist', 3: 'Dandvate Flowers'},
    'Wisteria Plant': {1: 'Pardeshi Flower Stall', 2: 'RAJ flower shop', 3: 'Florist'},
    'Rose': {1: 'The Trillion Roses Pune', 2: 'Ferns N Petals'},
    'Iris': {1: 'The Trillion Roses Pune', 2: 'Ferns N Petals'},
    'Ornamental Pink Muhly Grass': {1: 'Shrinivas Flower Stall', 2: 'Pardeshi Flower Stall'},
    'Tulip': {1: "Shamun's Flowers", 2: 'Ambika Florist'},
    'Sunflower': {1: 'Flower Link', 2: 'Mahalaxmi Nursery Harchiri'},
    'Daffodil': {1: 'Dandvate Flowers', 2: 'Mahajan Florist'},
    'Lili': {1: 'Ferns N Petals', 2: 'Riya Flowers', 3: 'RAJ flower shop'}
}

sellers_city_based = {	 	
    'pune_fruits': {1: 'Shree Krishna Vegetables and fruits', 2: 'VEGGOVILLA FRUITS AND VEGETABLES'},
    'pune_vegetables': {1:'Shree Krishna Vegetables and fruits', 2:'VEGGOVILLA FRUITS AND VEGETABLES'},
    'pune_flowers': {1: 'The Trillion Roses Pune', 2: 'Orchid Flora Nursery'},
    'sangli_fruits': {1: 'Gajanan Fruit Agency'},
    'sangli_vegetables': {1: 'Gajanan Fruit Agency'},
    'sangli_flowers': {1: 'Japanese Florist'},
    'nashik_fruits': {1: 'Ichhamani Fresh Vegetable And Fruits', 2: 'Vegetable & fruit', 3: 'Shree Bhulai Prajapati Vegetable & Fruit Company'},
    'nashik_vegetables': {1: 'Ichhamani Fresh Vegetable And Fruits', 2: 'Vegetable & fruit'},
    'nashik_flowers': {1: 'Ferns N Petals', 2: 'Dandvate Flowers'},
    'ahmadnagar_fruits': '',
    'ahmadnagar_vegetables': {1: 'Vegetable Market Yard'},
    'ahmadnagar_flowers': {1: 'Ambika Florist', 2: 'Just Flowers'},
    'solapur_fruits': {1: 'Sangola Agro Pvt Ltd'},
    'solapur_vegetables': {1: 'Sangola Agro Pvt Ltd'},
    'solapur_flowers': {1: 'Vinayak flower Shop'},
    'jalgaon_fruits': {1: 'Jalgaon Vegmart', 2: 'Quality Fresh Fruits & Vegetables'},
    'jalgaon_vegetables': {1: 'Jalgaon Vegmart', 2: 'Quality Fresh Fruits & Vegetables'},
    'jalgaon_flowers': {1: 'Jay Ambe Flowers Decorators'},
    'palghar_fruits': {1: 'Sharda vegetables and fruit shop'},
    'palghar_vegetables': {1: 'Sharda vegetables and fruit shop'},
    'palghar_flowers': {1: 'Pardeshi Flower Stall'},
    'ratnagiri_fruits': {1: 'Vegetable Market', 2:'Shree Mahalaxmi Bhaji Center'},
    'ratnagiri_vegetables': {1:'Shree Mahalaxmi Bhaji Center'},
    'ratnagiri_flowers': {1: 'Vrukshavalli Nursery & Garden', 2: 'Mahalaxmi Nursery Harchiri'},
    'mahabaleshwar_fruits': {1: ''},
    'mahabaleshwar_vegetables': {1, ''},
    'mahabaleshwar_flowers': {1, ''},
    'nagpur_fruits': {1: 'Shubham Sabji Merchant & Fruit Center', 2: 'Shetkari Bhandar - Farmer To Consumer Shop'},
    'nagpur_vegetables': {1: 'Shetkari Bhandar - Farmer To Consumer Shop'},
    'nagpur_flowers': {1: 'Mahajan Florist'},
    'khed_junnar_fruits': {1: ''},
    'khed_junnar_vegetables': {1: ''},
    'khed_junnar_flowers': {1: ''},


    # Then call it in respective functions and add it to context dict
    # And send to Html template and their try to connect to the map
}


@login_required
def plants(request):

    user=User.objects.filter(username=request.user)
    if len(user)!=0:
        plant=user[0].plant
        val=plant.name
        link=''

        if plant.Type=='Fruit':
            link=f'http://127.0.0.1:8000/Fruit-Name.html/{val}/'
        elif plant.Type=='Flower':
                link=f'http://127.0.0.1:8000/Flower-Name.html/{val}/'
        elif plant.Type=='Vegetable':
                link=f'http://127.0.0.1:8000/Vegetable-Name.html/{val}/'       


        context={
            'Uname':user[0].username,
            'Pname':plant.name,
            'link':link
        }
        
    else:
        context={
            'Uname':request.user,
            'Pname':"No Previous Search",
            'link':''
        }    
    return render(request, 'Plants.html',context)


def fertilizers(request):
    fertilizers=Fertilizer.objects.all()
    context={
        'fertilizer':fertilizers
    }
    return render(request, 'Fertilizers.html',context)


def fertilizers_name(request,val):
    Allfertizlizer=Fertilizer.objects.all()  
    fer=Fertilizer.objects.filter(name=val)
    seller=fer[0].seller.all()

    context = {'link': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d30155.296665082962!2d72.90283516450356!3d19.13343094957238!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7c7f189efc039%3A0x68fdcea4c5c5894e!2sIndian%20Institute%20of%20Technology%20Bombay!5e0!3m2!1sen!2sin!4v1633747503376!5m2!1sen!2sin",
    'len':len(seller),
    'seller':seller,
    'Allfertizlizer':Allfertizlizer,
    'fer':fer[0] 
    }

    return render(request, 'Fertilizers-Name.html',context)


# def fertilizers_name_details(request):

########################### FLOWER  SECTION ##########################################################

#FUNCTION FOR THE FLOWER HOME PAGE
def flower(request):
    #All the locations
    loc=Location.objects.all()

    #Details of vegetables
    q1 = Plant.objects.filter(Type='Flower')
   
    #context
    context={
        'list':q1,
        'location':loc
    }
    #Rendering the template
    return render(request, 'Flower.html',context)




#FUNCTION FOR RENDERING THE FLOWER FOR THE PARTICULAR CITY
def flower_city1(request,val):
    #for the query of the given location 
    loc=Location.objects.filter(cityname=val)
        

    #Details of plant in that location
    q1 = Plant.objects.filter(Type='Flower',location=loc[0])

    #Given Location
    location=Location.objects.all()

    #upadting the li with the address of the sellers
    li=[]
    for i in range(0,len(q1)):
       li.append(q1[i].seller.all())
    
    #converting the 2d list li into the 1d list in sellers
    sellers=[]
    for i in range(0,len(li)):
        for j in range(0,len(li[i])):  
            if li[i][j].residence_city==val:        
                sellers.append(li[i][j])

    #Removing the duplicates from the seller
    sellers = list(set(sellers)) 

    links = []
    if len(sellers) < 3:
        for i in range(0, len(sellers)):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])
    else:
        for i in range(0, 3):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])

    val = val.lower() + '_flowers'
    values = sellers_city_based[val]
    # print(values[1])
    coordinate = []
    for i in values:
        key = values[i]
        coordinate.append(individual_sellers[key])

    content = {}
    for i in range(0, len(sellers)):
        content[i] = f'''<h5>{sellers[i].name}</h5>
                    <p>Address: {sellers[i].address}</p><p>Phone No: {sellers[i].phone}</p>'''

    #passing the context
    context={
        'list':q1,
        'flower_length':len(q1),
        'sellers':sellers,
        'len':len(sellers),
        'location':location,
        'link': links,
        'coordinates': coordinate,
        'length': len(coordinate),
        'content': content
    }
    
    #Rendering the template 
    return render(request, 'Flower-City.html',context)




#FUNCTION FOR RENDERING THE CITY WHERE THE PARTICULAR FLOWER IS FOUND
def flower_name(request,val):
    #FOR GETTING THE PLANT INFORMATION
    q1 = Plant.objects.filter(Type='Flower',name=val)
    
    #SELLER OF THAT PARTICULAR PLANT
    sellers=q1[0].seller.all()

    if request.user.is_authenticated:
        users=User.objects.filter(username=request.user)
        length=len(User.objects.all())
        if len(users)==0:
            plant=Plant.objects.filter(name=val,Type='Flower')
            add=User(id=length+1,username=str(request.user),plant=plant[0])
            add.save()
        else:
            User.objects.get(id=users[0].id).delete()
            plant=Plant.objects.filter(name=val,Type='Flower')
            add=User(id=users[0].id,username=str(request.user),plant=plant[0])
            add.save()



    #Location where that particular plant is found
    location=q1[0].location.all()
    
    #LIST OF ALL THE FLOWERS
    flowers=Plant.objects.filter(Type='Flower')

    links = []
    if len(sellers) < 3:
        for i in range(0, len(sellers)):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])
    else:
        for i in range(0, 3):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])

    values = sellers_products_based[val]
    # print(values[1])
    coordinate = []
    for i in values:
        key = values[i]
        coordinate.append(individual_sellers[key])
    
    content = {}
    for i in range(0, len(sellers)):
        content[i] = f'''<h5>{sellers[i].name}</h5>
                    <p>Address: {sellers[i].address}</p><p>Phone No: {sellers[i].phone}</p>'''

    context = {
    'link': links,
    "flowers":flowers,
    'desc':q1[0],
    "sellers":sellers,
    'len':len(sellers),
    'location':location,
    'coordinates': coordinate,
    'content': content,
    'ex':content[0]
    }
    return render(request, 'Flower-Name.html', context)

################################## FRUIT SECTION ################################################

#FUNCTION FOR THE FRUIT HOME PAGE
def fruit(request):
    #All the locations
    loc=Location.objects.all()

    #Details of vegetables
    q1 = Plant.objects.filter(Type='Fruit')
   
    #context
    context={
        'list':q1,
        'location':loc
    }
    #Rendering the template
    return render(request, 'Fruit.html',context)




#FUNCTION FOR RENDERING THE FRUIT FOR THE PARTICULAR CITY
def fruit_city1(request,val):
    #for the query of the given location 
    loc=Location.objects.filter(cityname=val)
    
    #Details of plant in that location
    q1 = Plant.objects.filter(Type='Fruit',location=loc[0])

    #Given Location
    location=Location.objects.all()

    #upadting the li with the address of the sellers
    li=[]
    for i in range(0,len(q1)):
       li.append(q1[i].seller.all())
    
    #converting the 2d list li into the 1d list in sellers
    sellers=[]
    for i in range(0,len(li)):
        for j in range(0,len(li[i])):  
            if li[i][j].residence_city==val:        
                sellers.append(li[i][j])
    
    #Removing the duplictes from the sellers
    sellers = list(set(sellers))

    links = []
    if len(sellers) < 3:
        for i in range(0, len(sellers)):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])
    else:
        for i in range(0, 3):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])    

    val = val.lower() + '_flowers'
    values = sellers_city_based[val]
    # print(values[1])
    coordinate = []
    for i in values:
        key = values[i]
        coordinate.append(individual_sellers[key])
    
    content = {}
    for i in range(0, len(sellers)):
        content[i] = f'''<h5>{sellers[i].name}</h5>
                    <p>Address: {sellers[i].address}</p><p>Phone No: {sellers[i].phone}</p>'''
    #passing the context
    print(coordinate)
    context={
        'list':q1,
        'fruit_length':len(q1),
        'sellers':sellers,
        'len':len(sellers),
        'location':location,
        'link': links,
        'coordinates': coordinate,
        'content': content
    }
    #Rendering the template
    return render(request,'Fruit-City.html', context)




#FUNCTION FOR RENDERING THE CITY WHERE TAHT FRUIT IS FOUND
def fruit_name(request,val):
    #FOR GETTING THE PLANT INFORMATION
    q1 = Plant.objects.filter(Type='Fruit',name=val)
    
    #SELLER OF THAT PARTICULAR PLANT
    sellers=q1[0].seller.all()
    content = {}
    for i in range(0, len(sellers)):
        content[i] = f'''<h5>{sellers[i].name}</h5>
                    <p>Address: {sellers[i].address}</p><p>Phone No: {sellers[i].phone}</p>'''
    
    #FOR THE LAST SEARCH
    if request.user.is_authenticated:
        users=User.objects.filter(username=request.user)
        length=len(User.objects.all())
        if len(users)==0:
            plant=Plant.objects.filter(name=val,Type='Fruit')
            add=User(id=length+1,username=str(request.user),plant=plant[0])
            add.save()
        else:
            User.objects.get(id=users[0].id).delete()
            plant=Plant.objects.filter(name=val,Type='Fruit')
            add=User(id=users[0].id,username=str(request.user),plant=plant[0])
            add.save()



    # print(links)

    #Location where that particular plant is found
    location=q1[0].location.all()
    
    #LIST OF ALL THE FLOWERS
    fruit=Plant.objects.filter(Type='Fruit')

    links = []
    if len(sellers) < 3:
        for i in range(0, len(sellers)):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])
    else:
        for i in range(0, 3):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])

    val = val.lower()
    values = sellers_products_based[val]
    # print(values[1])
    coordinate = []
    for i in values:
        key = values[i]
        coordinate.append(individual_sellers[key])
    
    context = {
    'link': links,
    "fruit":fruit,
    'desc':q1[0],
    "sellers":sellers,
    'len':len(sellers),
    'location':location,
    'coordinates': coordinate,
    'content': content
    }
    return render(request, 'Fruit-Name.html', context)


########################### VEGETABLE SECTION ##########################################

#FUNCTION FOR THE VEGETABLE HOME PAGE
def vegetable(request):
    #All the locations
    loc=Location.objects.all()

    #Details of vegetables
    q1 = Plant.objects.filter(Type='Vegetable')
   
    #context
    context={
        'list':q1,
        'location':loc
    }
    #Rendering the template
    return render(request, 'Vegetable.html',context)




#FUNCTION FOR RENDERNG THE CITY WHERE THAT VEGETABLE IS FOUND
def vegetable_name(request,val):
    #FOR GETTING THE PLANT INFORMATION
    q1 = Plant.objects.filter(Type='Vegetable',name=val)
    
    #SELLER OF THAT PARTICULAR VEGETABLE
    sellers=q1[0].seller.all()
    content = {}
    for i in range(0, len(sellers)):
        content[i] = f'''<h5>{sellers[i].name}</h5>
                    <p>Address: {sellers[i].address}</p><p>Phone No: {sellers[i].phone}</p>'''

    #Location where that particular plant is found
    location=q1[0].location.all()
    
    #FOR THE LAST SEARCH
    if request.user.is_authenticated:
        users=User.objects.filter(username=request.user)
        length=len(User.objects.all())
        if len(users)==0:
            plant=Plant.objects.filter(name=val,Type='Vegetable')
            add=User(id=length+1,username=str(request.user),plant=plant[0])
            add.save()
        else:
            User.objects.get(id=users[0].id).delete()
            plant=Plant.objects.filter(name=val,Type='Vegetable')
            add=User(id=users[0].id,username=str(request.user),plant=plant[0])
            add.save()



    #LIST OF ALL THE xFLOWERS
    vegetable=Plant.objects.filter(Type='Vegetable')

    links = []
    if len(sellers) < 3:
        for i in range(0, len(sellers)):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])
    else:
        for i in range(0, 3):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])
    
    val = val.lower()
    values = sellers_products_based[val]
    # print(values[1])
    coordinate = []
    for i in values:
        key = values[i]
        coordinate.append(individual_sellers[key])

    context = {
    'link': links,
    "vegetable":vegetable,
    'desc':q1[0],
    'len':len(sellers),
    "sellers":sellers,
    'location':location,
    'coordinates': coordinate,
    'content': content
    }
    return render(request, 'Vegetable-Name.html',context)




#FUNCTION FOR RENDERING THE VEGETABLE FOR THE PARTICULAR CITY
def vegetable_city1(request,val):
     #for the query of the given location 
    loc=Location.objects.filter(cityname=val)
    
    #Details of plant in that location
    q1 = Plant.objects.filter(Type='Vegetable',location=loc[0])

    #Given Location
    location=Location.objects.all()

    #upadting the li with the address of the sellers
    li=[]
    for i in range(0,len(q1)):
       li.append(q1[i].seller.all())
    
    #converting the 2d list li into the 1d list in sellers
    sellers=[]
    for i in range(0,len(li)):
        for j in range(0,len(li[i])):  
            if li[i][j].residence_city==val:        
                sellers.append(li[i][j])

    
    #Removing the duplictes from the sellers
    sellers = list(set(sellers))
    
    links = []
    if len(sellers) < 3:
        for i in range(0, len(sellers)):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])
    else:
        for i in range(0, 3):
            # print(sellers[i].name)
            links.append(individual_sellers_link[sellers[i].name])

    val = val.lower() + '_vegetables'
    values = sellers_city_based[val]
    # print(values[1])
    coordinate = []
    for i in values:
        key = values[i]
        coordinate.append(individual_sellers[key])

    content = {}
    for i in range(0, len(sellers)):
        content[i] = f'''<h5>{sellers[i].name}</h5>
                    <p>Address: {sellers[i].address}</p><p>Phone No: {sellers[i].phone}</p>'''
    #passing the context

    context={
        'list':q1,
        'sellers':sellers,
        'vegetable_length':len(q1),
        'len':len(sellers),
        'location':location,
        'link': links,
        'coordinates': coordinate,
        'content': content
    }
    
    #Rendering the template    
    return render(request, 'Vegetable-City.html',context)


