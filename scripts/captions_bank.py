#!/usr/bin/env python3
"""Caption bank for Aurelian Canvas Auto-Poster. Pure data - used by gen_schedule.py."""

# Per-art Pinterest titles (<=100 chars each, keyword-led) and description seeds.
# IG captions are complete (hook + body + CTA). Hashtag sets are 12 tags.

SHARED_DESC_INFO = [
    "Instant digital download - no waiting, no shipping, no physical item arrives. Print at home, at a local print shop, or upload to an online print service and frame it your way.",
    "You receive high-resolution files ready to print in multiple sizes, in both portrait and landscape orientation, so it fits your wall and your frame perfectly.",
    "Printable art is the easiest decor upgrade: buy today, print tonight, hang it this weekend. Works beautifully in standard frames from any home store.",
    "Personal-use license included. Print it as many times as you like for your own home or as a thoughtful housewarming gift. Questions? Message us on Instagram @aureliancanvas.",
]

ART_CONTENT = {
    "fresco-of-the-gods": {
        "pin_titles": [
            "Renaissance Fresco Wall Art Printable | Blue Gold Angel Ceiling Print",
            "Antique Angel Fresco Print | Classical Ceiling Wall Art Download",
            "Old World Italian Fresco Art | Heavenly Angels Printable Decor",
            "Blue and Gold Renaissance Art Print | Fresco Angel Digital Download",
            "Heavenly Ceiling Mural Art | Antique Fresco Printable Wall Decor",
            "Classical Angel Wall Art | Renaissance Fresco Instant Download",
        ],
        "desc_seed": "Bring the Sistine-adjacent drama of a Renaissance ceiling into your home. This antique-style fresco of blue-robed angels with golden halos was created as a printable wall art download - the cracked plaster texture and aged gold leaf glow look stunning above a dining table, in an entryway, or as the heart of a gallery wall.",
        "alt_hooks": [
            "Renaissance angels in aged gold and antique blue - a ceiling masterpiece you can hang anywhere.",
            "Old-world fresco art with cracked plaster texture and heavenly golden light.",
            "Classical angel fresco in antique blue and gold, ready to print and frame.",
            "A Renaissance ceiling you can actually own - printable fresco wall art.",
            "Heavenly fresco wall art in blue and gold for old-world inspired rooms.",
            "Antique angel mural style art, instantly downloadable and printable.",
        ],
        "ig_image_caps": [
            "Some ceilings were painted to be looked up at. This is one of them.\n\nRenaissance angels, cracked plaster, antique gold - printed art that feels like it survived 500 years. It turns any wall into the reason guests stop talking mid-sentence.\n\nInstant download - print tonight, hang this weekend. Link in bio.",
            "500 years of beauty, hanging on a modern wall.\n\nThis fresco was made for people who fall in love with museums. Blue-robed angels, golden halos, that aged ceiling glow - now in a printable download that fits your frames.\n\nInstant download, portrait + landscape. Link in bio.",
            "POV: your dining room finally has a ceiling worth copying.\n\nA classical angel fresco with old-world texture and warm gold light. It makes candlelit dinners feel like they were staged in an Italian palazzo.\n\nPrintable wall art, instant download. Link in bio.",
            "This fresco has watched empires rise. Now it watches your hallway.\n\nAntique blue and gold, hand-cracked texture, heavenly angels - art with the soul of a cathedral and the convenience of a download.\n\nInstant printable, ready for your favorite frame. Link in bio.",
            "Candlelit dinners just got an upgrade.\n\nOur Renaissance angel fresco glows in warm evening light the way it was painted to. One wall, one print, and the whole room feels like old money.\n\nDownload, print, frame - tonight. Link in bio.",
            "They painted heaven once. We print it for your walls.\n\nA heavenly fresco of angels in flowing blue, finished in antique gold - created for homes that want the museum look without the museum price.\n\nInstant download, both orientations included. Link in bio.",
        ],
        "ig_reel_caps": [
            "Watch an empty wall turn into a Renaissance ceiling.\n\nNo hammer, no nails, no 500-year wait - just a print, a frame, and a room that suddenly has a story. Swipe up in our bio to make it yours.\n\nWhich wall in your home deserves this? Tell us below.",
            "That moment the light hits the gold leaf and the whole room changes.\n\nOur fresco was designed to glow exactly like the old masters intended - warm, aged, and quietly dramatic.\n\nInstant download from the link in bio. Your ceiling-light viewing starts tonight.",
            "Museums charge admission. Your wall just needs a frame.\n\nA Renaissance angel fresco with real age and texture, delivered instantly as a printable file. Print it, frame it, and let the compliments roll in.\n\nLink in bio - both portrait and landscape included.",
        ],
        "hashtags": "#renaissanceart #frescowallart #printablewallart #antiquedecor #blueandgolddecor #classicalart #oldworlddecor #wallartdownload #luxuryhomedecor #gallerywall #angelart #homedecorideas",
    },
    "liquidonyx": {
        "pin_titles": [
            "Black Marble Wall Art Printable | Silver Vein Abstract Luxury Decor",
            "Liquid Onyx Abstract Print | Black Silver Modern Wall Art Download",
            "Dark Luxury Wall Art | Black Onyx Marble Printable Abstract",
            "Modern Black Abstract Art | Molten Silver Marble Print Download",
            "Moody Luxury Decor Art | Black Silver Abstract Printable Wall Art",
            "Executive Office Wall Art | Black Marble Silver Abstract Print",
        ],
        "desc_seed": "Liquid Onyx is black marble with a heartbeat - molten silver veins cutting through deep onyx stone. A modern luxury abstract that anchors a minimalist living room, a moody bedroom, or an executive office. Printed large, it reads like sculpted stone; up close, the metallic flow pulls you in.",
        "alt_hooks": [
            "Black marble with molten silver veins - quiet luxury for modern walls.",
            "Liquid metal flowing through onyx stone, frozen as printable art.",
            "Dark, dramatic, and endlessly elegant - abstract onyx wall art.",
            "The statement piece every moody minimalist room is missing.",
            "Silver veins on deep black stone - modern luxury as a download.",
            "One print, whole-room mood: liquid onyx abstract wall art.",
        ],
        "ig_image_caps": [
            "Some rooms whisper. This one doesn't need to.\n\nLiquid Onyx - black marble split by molten silver. It's the kind of art that makes a minimalist room feel expensive and an expensive room feel complete.\n\nInstant printable download, portrait + landscape. Link in bio.",
            "Zoom in. Those aren't cracks - they're silver veins.\n\nA luxury abstract that behaves like real stone: matte black depth with liquid metal light. Perfect over a console, a bed, or behind your desk.\n\nDownload, print, frame tonight. Link in bio.",
            "Dark academia called. It wants its masterpiece back.\n\nLiquid Onyx is moody modern art at its best - black marble texture with flowing silver that catches every bit of light in the room.\n\nInstant download, no shipping wait. Link in bio.",
            "The art equivalent of a black card.\n\nUnderstated. Precise. Unmissable. This black and silver abstract works in living rooms, offices, and anywhere that needs quiet power on the wall.\n\nPrintable art, instant download. Link in bio.",
            "Every luxury interior needs one dark, dramatic anchor.\n\nThis is it. Liquid Onyx - molten silver across deep onyx black - styled here in a modern living room that lets it speak.\n\nWhich room gets yours? Link in bio.",
            "Made for walls that mean business.\n\nLiquid Onyx in a working space: sharp suit energy, zero clutter, one unforgettable print. Digital download means it's on your wall this week.\n\nLink in bio to grab it.",
        ],
        "ig_reel_caps": [
            "From plain black wall to liquid luxury in one frame.\n\nThis is Liquid Onyx - black marble with molten silver veins that shimmer as the light moves. No waiting for delivery: buy, print, hang, done.\n\nWhich wall would you put it on? Link in bio.",
            "The light moves. The silver moves with it.\n\nThat's the magic of Liquid Onyx - a metallic abstract print that looks different at every hour of the day. One download, endless moods.\n\nInstant printable. Link in bio.",
            "POV: you finally found art that matches the rest of the room's energy.\n\nBlack. Silver. Silent confidence. Liquid Onyx is the modern luxury abstract your space has been waiting for.\n\nGrab the instant download - link in bio.",
        ],
        "hashtags": "#blackwallart #marbleprint #modernluxurydecor #abstractwallart #printablewallart #darkinteriors #minimalistdecor #silverandblack #moodydecor #wallartdownload #executiveoffice #luxuryhomedecor",
    },
    "the-titanium-wealth": {
        "pin_titles": [
            "Navy Blue Gold Wall Art Printable | Abstract Luxury Modern Decor",
            "Gold Streak Abstract Print | Navy Blue Textured Wall Art Download",
            "Blue Gold Palette Knife Art | Abstract Textured Printable Decor",
            "Modern Luxe Wall Art | Navy Gold Abstract Printable Download",
            "Deep Blue Gold Leaf Abstract | Luxury Printable Wall Art Print",
            "Glam Living Room Art | Navy Blue Gold Abstract Wall Decor Print",
        ],
        "desc_seed": "The Titanium Wealth is deep navy paint split by bold gold streaks - a palette-knife abstract with real texture you can almost feel through the frame. Navy and gold is the classic power pairing of interior design: confident in a living room, grounding in a bedroom, sharp in a home office.",
        "alt_hooks": [
            "Deep navy paint, bold gold streaks - wealth energy for modern walls.",
            "Palette-knife texture you can almost feel, in navy and gold.",
            "The power pairing: midnight blue and molten gold abstract art.",
            "Navy and gold abstract art with real painterly texture.",
            "Rich, deep, dramatic - a luxury abstract for statement walls.",
            "Midnight blue meets gold rush in this textured abstract print.",
        ],
        "ig_image_caps": [
            "Navy and gold. The two colors that never lose.\n\nThe Titanium Wealth brings palette-knife texture and midnight depth to your wall - it reads luxury from across the room and craft from up close.\n\nInstant download, portrait + landscape. Link in bio.",
            "Texture you can feel with your eyes.\n\nBold gold strokes carve through deep navy in this modern abstract. In a gold frame on a light wall? Unstoppable.\n\nPrintable art, instant download. Link in bio.",
            "Your living room called. It wants this over the sofa.\n\nNavy blue and gold is the oldest luxury pairing in design - and this textured abstract does it justice without saying a word.\n\nDownload, print, hang this weekend. Link in bio.",
            "Old money colors. New money ease.\n\nThe Titanium Wealth is instant-download art: buy it now, print it at any size, and let your wall do the flexing.\n\nLink in bio - both orientations included.",
            "Some art decorates a room. This one commands it.\n\nDeep navy with gold streaks that catch the evening light exactly right. Made for homes that take their walls seriously.\n\nInstant printable download. Link in bio.",
            "Behind every good sofa is a great abstract.\n\nOurs is navy, gold, and textured like the paint is still wet. The Titanium Wealth - modern luxury for statement walls.\n\nGrab it in the link in bio.",
        ],
        "ig_reel_caps": [
            "Watch the gold catch the light on this one.\n\nThe Titanium Wealth - thick navy texture, bold gold streaks, zero shipping wait. It's a digital download that prints gallery-size.\n\nWhich wall in your home is worthy? Link in bio.",
            "From blank wall to boardroom energy in one print.\n\nNavy blue and gold, palette-knife texture, instant download. This is how modern rooms get expensive-looking walls.\n\nLink in bio to download and print tonight.",
            "The room isn't finished until this is on the wall.\n\nDeep navy. Molten gold. Real texture. The Titanium Wealth is the abstract your space has been asking for - printable in any size you need.\n\nInstant download at the link in bio.",
        ],
        "hashtags": "#navyandgold #abstractwallart #luxurywallart #printablewallart #golddecor #modernabstract #glamhomedecor #wallartdownload #texturedart #livingroomdecor #bluedecor #homedecorideas",
    },
    "the-golden-empress": {
        "pin_titles": [
            "Klimt Style Wall Art Printable | Gold Leaf Woman Portrait Print",
            "Gold Leaf Portrait Art | Royal Blue Peacock Printable Wall Decor",
            "Art Nouveau Woman Print | Golden Empress Klimt Inspired Wall Art",
            "Glam Gold Portrait Printable | Art Nouveau Luxury Wall Art",
            "Jewel Tone Wall Art | Gold Blue Peacock Portrait Digital Download",
            "Luxury Feminine Wall Decor | Klimt Gold Portrait Printable Art",
        ],
        "desc_seed": "Inspired by the golden age of Klimt, The Golden Empress is a regal woman's portrait finished in shimmering gold leaf tones, royal blues and peacock jewelry. It belongs above a vanity, in a dressing room, or anywhere that deserves a jewel-box moment. Fans of Art Nouveau and gilded portraits: this is your piece.",
        "alt_hooks": [
            "A Klimt-inspired empress in gold leaf and royal blue - regal printable art.",
            "Golden jewelry tones, jewel-blue background, one unforgettable portrait.",
            "Art Nouveau glamour for walls that like a little drama.",
            "The Golden Empress: gilded portrait art, instantly downloadable.",
            "Peacock blues and shimmering gold - feminine luxury in a print.",
            "A portrait that dresses the whole room in gold.",
        ],
        "ig_image_caps": [
            "Gustav Klimt walked so this empress could reign.\n\nGold leaf tones, royal blue, peacock jewelry - a portrait that turns a bedroom wall into a jewelry box. Art Nouveau drama, instant-download convenience.\n\nLink in bio to make her yours.",
            "Every home needs one room that feels like a palace.\n\nStart with The Golden Empress - a gilded, Klimt-inspired portrait that glows in lamplight and stops every scroll.\n\nInstant printable download. Link in bio.",
            "She's been guarding palaces for centuries. Your wall looks worthy.\n\nThe Golden Empress in gold and royal blue - feminine, regal, and printed at whatever size your space demands.\n\nDownload, print, frame. Link in bio.",
            "Jewel tones + gold leaf = the glow-up your gallery wall needs.\n\nThis Klimt-style empress portrait pairs beautifully with gold frames, velvet textures and moody evenings.\n\nInstant download, portrait + landscape. Link in bio.",
            "Not all queens wear crowns. Some hang on walls.\n\nThe Golden Empress - a gold leaf style portrait with peacock blues that brings Art Nouveau luxury to modern homes.\n\nWhich room does she rule? Link in bio.",
            "POV: your dressing room finally matches your energy.\n\nRegal, radiant, and ready to print - The Golden Empress is downloadable art for people who love a little gold with their glamour.\n\nLink in bio.",
        ],
        "ig_reel_caps": [
            "The way the gold moves when the light hits her...\n\nThe Golden Empress - a Klimt-inspired portrait in gold leaf tones and royal blue, delivered instantly as a printable file. She was made for lamplit evenings.\n\nMake her yours - link in bio.",
            "From darkness into gold, just like that.\n\nWatch her emerge. The Golden Empress is printable Art Nouveau glamour for walls that deserve a queen.\n\nInstant download, both orientations. Link in bio.",
            "Some portraits hang. This one reigns.\n\nGold, blue, and unapologetically ornate - The Golden Empress is the statement your gallery wall has been waiting for.\n\nDownload her today at the link in bio.",
        ],
        "hashtags": "#klimtinspired #goldleafart #artnouveau #printablewallart #glamdecor #portraitart #jeweltones #luxurywallart #peacockdecor #wallartdownload #femininedecor #goldhomedecor",
    },
    "the-golden-lion": {
        "pin_titles": [
            "Gold Lion Wall Art Printable | Luxury Masculine Office Decor Print",
            "Textured Lion Portrait Print | Gold Animal Art Digital Download",
            "Executive Office Wall Art | Golden Lion Palette Knife Print",
            "Majestic Lion Wall Decor | Gold Textured Printable Animal Art",
            "Study Room Lion Art Print | Luxury Gold Wildlife Wall Decor",
            "Statement Wall Art Lion | Gold Texture Printable Office Decor",
        ],
        "desc_seed": "The Golden Lion is a palette-knife textured portrait of the king himself - thick golden strokes, an unblinking gaze, and the presence of a boardroom and a savannah at once. The definitive piece for executive offices, studies, and any room that needs a silent statement of power.",
        "alt_hooks": [
            "A lion in textured gold - the office art that means business.",
            "Palette-knife gold strokes, one unblinking gaze.",
            "Presence, printed: the Golden Lion for walls that lead.",
            "Majestic, masculine, metallic - lion art in luminous gold.",
            "The king of the wall, rendered in thick golden texture.",
            "Executive energy in animal form - gold lion printable art.",
        ],
        "ig_image_caps": [
            "Kings don't ask for attention. The room just gives it.\n\nThe Golden Lion - palette-knife texture, molten gold, one serious stare. The final piece your office or study was missing.\n\nInstant download, portrait + landscape. Link in bio.",
            "The most-asked-about piece in the entire collection.\n\nTextured gold lion, carved like the paint is still wet. It belongs above a desk, behind a chair, or anywhere decisions get made.\n\nPrintable art, instant download. Link in bio.",
            "Your office has a chair, a desk, and a silence. Fix the silence.\n\nThe Golden Lion fills a wall with quiet authority - thick gold texture that photographs as expensive as it looks.\n\nDownload and print tonight. Link in bio.",
            "They call him the king for a reason.\n\nA gilded lion portrait with real palette-knife texture - printed large, he takes over the room in the best way.\n\nLink in bio for the instant download.",
            "Masculine decor done right: one animal, one color, one statement.\n\nThe Golden Lion in textured gold - for studies, offices, and living rooms that refuse to be boring.\n\nGrab the download at the link in bio.",
            "Some walls have art. This one has a presence.\n\nThe Golden Lion is the print guests remember long after they leave. Digital file, instant access, any print size.\n\nLink in bio.",
        ],
        "ig_reel_caps": [
            "He doesn't roar. He doesn't need to.\n\nThe Golden Lion - thick gold texture, one unblinking gaze, instant download. The office upgrade that takes ten minutes to hang and years to forget.\n\nWhich wall is his? Link in bio.",
            "Watch the texture work as the light moves across the gold.\n\nThat's real palette-knife style depth in The Golden Lion - printable in sizes big enough to own the whole room.\n\nLink in bio to download him now.",
            "Boring office to executive den in one frame.\n\nThe Golden Lion: molten gold, textured strokes, silent authority. Buy, print, hang - today.\n\nInstant download at the link in bio.",
        ],
        "hashtags": "#lionwallart #golddecor #masculinedecor #officeart #printablewallart #animalportrait #executiveoffice #studydecor #luxurywallart #goldlion #wallartdownload #statementart",
    },
    "she-stands-at-the-old-door": {
        "pin_titles": [
            "Autumn Cottage Wall Art Printable | Watercolor Countryside Print",
            "Cottagecore Wall Art | Autumn Door Watercolor Digital Download",
            "Rustic Farmhouse Print | Countryside Autumn Watercolor Wall Art",
            "Storybook Cottage Print | Fall Countryside Printable Wall Decor",
            "Cozy Autumn Home Decor | Watercolor Old Door Printable Art",
            "Vintage Countryside Wall Art | Autumn Watercolor Instant Download",
        ],
        "desc_seed": "She stands at the old door, autumn light spilling across the fields. This storybook watercolor captures the exact feeling of a cool October morning in the countryside - golden trees, a worn wooden door, and the sense that a new chapter is about to begin. Perfect for cottagecore rooms, reading corners, and cozy entryways.",
        "alt_hooks": [
            "An autumn door, golden fields, and one quiet storybook moment.",
            "Cottagecore watercolor art for homes that love soft light.",
            "The countryside is calling - and it fits your frame.",
            "Autumn in watercolor: worn wood, golden leaves, open door.",
            "A storybook scene you can hang in your hallway.",
            "Cozy, golden, and nostalgic - printable autumn watercolor art.",
        ],
        "ig_image_caps": [
            "Every old door is a question. She's finally answering.\n\nA storybook watercolor of autumn light, golden fields and one worn wooden door - cottagecore art that makes a hallway feel like a novel.\n\nInstant download, portrait + landscape. Link in bio.",
            "October lives here all year round.\n\nThis countryside watercolor brings warm fall tones and quiet storybook energy to any wall - especially next to your reading chair.\n\nPrintable art, instant download. Link in bio.",
            "POV: you opened a door and the whole world was golden.\n\nShe Stands at the Old Door - a soft watercolor print for homes that believe walls should tell stories.\n\nLink in bio to download and print.",
            "Some art matches your decor. This art matches your mood.\n\nGolden autumn light, an old door, a beginning about to happen - watercolor printed from an instant download.\n\nCozy homes only. Link in bio.",
            "The hallway called. It wants to be a storybook now.\n\nWarm watercolor, autumn countryside, and a door that's clearly about to open. Cottagecore printable art at its coziest.\n\nGrab it at the link in bio.",
            "For everyone whose favorite season is golden.\n\nThis watercolor keeps October on your wall through every month - soft, nostalgic and ready to frame.\n\nInstant download, link in bio.",
        ],
        "ig_reel_caps": [
            "She's been waiting at that door all autumn. Are you coming?\n\nA storybook watercolor that turns any wall into the first page of a novel. Cottagecore printable art, instant download.\n\nWhere would you hang her? Link in bio.",
            "The door opens. The light spills. The room changes.\n\nThis is She Stands at the Old Door - a warm autumn watercolor for cottage souls and cozy corners.\n\nInstant printable download at the link in bio.",
            "Not all heroes walk through doors. Some hang beside them.\n\nGolden fields, worn wood, watercolor light - this print turns fall into a permanent guest.\n\nDownload, print, cozy up. Link in bio.",
        ],
        "hashtags": "#cottagecoredecor #autumnwallart #watercolorprint #printablewallart #farmhousedecor #storybookart #countrystyle #cozyhome #falldecor #wallartdownload #vintageprint #homedecorideas",
    },
    "the-letter": {
        "pin_titles": [
            "Rainy Day Wall Art Printable | Candlelight Reading Nook Watercolor",
            "Cozy Reading Nook Art | Rainy Evening Watercolor Digital Download",
            "Vintage Letter Writing Print | Cottagecore Rainy Night Wall Art",
            "Candlelight Watercolor Print | Cozy Rain Window Printable Decor",
            "Book Lover Gift Art | Rainy Evening Reading Watercolor Print",
            "Warm Cottage Wall Art | Vintage Letter Watercolor Printable Decor",
        ],
        "desc_seed": "Rain on the window, a candle on the desk, and a letter worth reading twice. The Letter is a cozy watercolor for quiet evenings - warm candlelight against a blue-grey storm, made for reading nooks, bedrooms, and every corner that feels like a deep breath. Pairs beautifully with She Stands at the Old Door as a storybook set.",
        "alt_hooks": [
            "Rain, candlelight, and a letter worth reading twice.",
            "A watercolor that sounds like rain on the window.",
            "Cozy evenings, printed: candlelit watercolor wall art.",
            "The coziest corner of the internet, now on your wall.",
            "For rainy-day souls and slow-evening hearts.",
            "One candle, one letter, one perfectly quiet evening.",
        ],
        "ig_image_caps": [
            "Some letters are read once. The good ones, twice.\n\nThe Letter - a candlelit watercolor of rain and quiet evenings, made for reading nooks and rainy-day souls.\n\nInstant download, portrait + landscape. Link in bio.",
            "The sound of rain, the warmth of a candle - in wall form.\n\nThis cozy watercolor turns any corner into the seat by the window on a stormy night. Cottagecore comfort, printable in minutes.\n\nLink in bio to download.",
            "POV: it's raining, the power's out, and you're exactly where you want to be.\n\nThe Letter is a watercolor for people who collect quiet evenings.\n\nPrintable art, instant download. Link in bio.",
            "Book lovers: this one's for your reading nook.\n\nA rain-splattered window, warm candlelight, and one unread letter - The Letter is storybook art for slow evenings.\n\nGrab it at the link in bio.",
            "Your rainiest mood deserves matching art.\n\nSoft blues, warm golds, one flickering flame - The Letter brings cozy melancholy to bedrooms and nooks.\n\nInstant download. Link in bio.",
            "Cozy isn't a season. It's a wall decision.\n\nThe Letter - candlelit rainy-evening watercolor, ready to print and hang before the next storm.\n\nLink in bio.",
        ],
        "ig_reel_caps": [
            "Listen closely - you can almost hear the rain.\n\nThe Letter, a candlelit watercolor for quiet evenings and cozy corners. Instant printable download, ready before your kettle boils.\n\nWhere's your reading nook? Link in bio.",
            "One candle. One letter. One evening that belongs to you.\n\nThe Letter is rainy-day watercolor art for walls that value peace. Download, print, slow down.\n\nLink in bio.",
            "The coziest scene we've ever painted - and yes, it's a download.\n\nRain on the glass, gold on the desk, a story on the page. The Letter is cottagecore comfort as printable art.\n\nGrab it at the link in bio.",
        ],
        "hashtags": "#cozywallart #rainydayvibes #watercolorprint #printablewallart #readingnook #cottagecoreaesthetic #candlelight #bookloversdecor #vintageillustration #wallartdownload #cozydecor #homedecorideas",
    },
}

# Bundles: 4 collage pins (title, desc) + IG captions
BUNDLE_PINS = {
    "gold-series-duo": {
        "title": "Gold Wall Art Duo Set | Golden Empress + Golden Lion Printable",
        "desc": "Two golden statement pieces, one set. The Golden Empress (Klimt-style gold leaf portrait) and The Golden Lion (textured gold palette-knife portrait) as matching printable wall art. Save versus buying separately - instant download, portrait and landscape files for every frame. Perfect for a matching living room and office set, or a his-and-hers gold wall.",
    },
    "luxe-abstract-duo": {
        "title": "Black Navy Abstract Set | Liquid Onyx + Titanium Wealth Printables",
        "desc": "The modern luxury pair: Liquid Onyx (black marble with molten silver veins) and The Titanium Wealth (deep navy with bold gold streaks). Two textured abstracts, one instant-download set - save versus buying separately. Ideal for a dark-luxe living room, a moody bedroom, or a masculine office that needs two coordinated walls.",
    },
    "storybook-diptych": {
        "title": "Cozy Watercolor Set | Old Door + The Letter Storybook Printables",
        "desc": "Two chapters of the same quiet story: She Stands at the Old Door (autumn countryside watercolor) and The Letter (rainy candlelight reading scene). A cottagecore diptych set as instant-download printables - save versus buying separately. Made for reading nooks, hallways, and homes that love soft, storybook walls.",
    },
    "full-collection": {
        "title": "All 7 Wall Art Prints Bundle | Luxury Printable Collection Download",
        "desc": "The complete Aurelian Canvas collection - all seven artworks in one instant-download bundle: Renaissance fresco angels, black onyx marble, navy-gold abstract, Klimt-style empress, golden lion, and two storybook watercolors. Seven rooms, seven moods, one price - save over 40% versus buying separately. Portrait and landscape files included for every piece.",
    },
}

BUNDLE_IG_CAPS = {
    "gold-series-duo": "Gold on gold. 👑🦁\n\nThe Gold Series Duo: The Golden Empress + The Golden Lion as one matching set - two statement walls, one price that beats buying separately.\n\nInstant download, all orientations. Link in bio.",
    "luxe-abstract-duo": "Two darks. Twice the drama. 🖤\n\nThe Luxe Abstract Duo pairs Liquid Onyx with The Titanium Wealth - black-silver and navy-gold in one coordinated set.\n\nSave versus singles, download instantly. Link in bio.",
    "storybook-diptych": "One story. Two prints. 🍂📖\n\nThe Storybook Diptych: She Stands at the Old Door + The Letter - autumn light outside, candlelight inside.\n\nA cottagecore set, instant download, link in bio.",
    "full-collection": "Every wall in the house just got a plan. 🏛️👑🦁🖤💎🍂🕯️\n\nThe Full Collection: all 7 Aurelian Canvas artworks in one bundle - over 40% off versus buying separately.\n\nRenaissance to watercolor, instant download. Link in bio.",
}

REPEAT_PS = [
    "P.S. Instant download means it's on your wall this week, not this month.",
    "P.S. Both portrait and landscape files come with every order.",
    "P.S. Bundle it with a matching piece and save - see the link in bio.",
    "P.S. Printed on good paper with a good frame, nobody believes it's a download.",
]
