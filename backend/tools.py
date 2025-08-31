book_summaries_dict = {
    "Hobbitul": (
        "Bilbo Baggins, un hobbit confortabil și fără aventuri, este luat prin surprindere atunci când este invitat într-o misiune de a recupera comoara piticilor păzită de dragonul Smaug. "
        "Pe parcursul călătoriei, el descoperă curajul și resursele interioare pe care nu știa că le are. "
        "Povestea este plină de creaturi fantastice, prietenii neașteptate și momente tensionate."
    ),
    "1984": (
        "Romanul lui George Orwell descrie o societate distopică aflată sub controlul total al statului. "
        "Oamenii sunt supravegheați constant de „Big Brother”, iar gândirea liberă este considerată crimă. "
        "Winston Smith, personajul principal, încearcă să reziste acestui regim opresiv. "
        "Este o poveste despre libertate, adevăr și manipulare ideologică."
    ),
    "Micul Prinț": (
        "Un copil călătorește pe diferite planete, descoperind lecții despre viață, iubire și prietenie. "
        "Povestea explorează inocența, curiozitatea și importanța relațiilor. "
        "Este o meditație poetică asupra sensului vieții și a valorilor umane."
    ),
    "Enigma Otiliei": (
        "Otilia, o tânără inteligentă și sensibilă, navighează intrigile unei familii bucureștene, în timp ce Felix încearcă să-și găsească locul în lume. "
        "Romanul explorează relațiile de familie, dragostea și maturizarea. "
        "Este o frescă socială a Bucureștiului de la începutul secolului XX."
    ),
    "Moromeții": (
        "Viața unei familii de țărani din satul românesc, cu provocările sociale și economice ale epocii. "
        "Ilie Moromete încearcă să mențină unitatea familiei în fața schimbărilor. "
        "Romanul evidențiază tradițiile rurale și conflictul dintre generații."
    ),
    "Ion": (
        "Ion, un țăran ambițios, luptă pentru pământ și statut social, sacrificând dragostea adevărată. "
        "Romanul explorează dorința de avere, conflictele morale și viața rurală. "
        "Este o analiză profundă a psihologiei personajului principal."
    ),
    "Amintiri din copilărie": (
        "Povestiri pline de umor și nostalgie despre copilăria autorului în satul Humulești. "
        "Personajele și întâmplările reflectă viața rurală și tradițiile românești. "
        "Este o celebrare a inocenței și bucuriei copilăriei."
    ),
    "Baltagul": (
        "Vitoria Lipan pornește într-o călătorie plină de pericole pentru a-și găsi soțul dispărut. "
        "Romanul evidențiază curajul, determinarea și credința unei femei. "
        "Este o poveste despre dreptate și tradiții montane."
    ),
    "Cel mai iubit dintre pământeni": (
        "Viața lui Victor Petrini, marcată de suferință, dragoste și lupta pentru supraviețuire într-o societate opresivă. "
        "Romanul explorează libertatea, iubirea și rezistența umană. "
        "Este o meditație asupra condiției umane."
    ),
    "Ultima noapte de dragoste, întâia noapte de război": (
        "Ștefan Gheorghidiu trăiește drama iubirii și a războiului, reflectând asupra sensului existenței. "
        "Romanul analizează relațiile de cuplu, identitatea și impactul războiului asupra individului. "
        "Este o poveste despre sacrificiu și căutarea sensului vieții."
    ),
}

def get_summary_by_title(title: str) -> str:
    """
    Returnează rezumatul complet pentru titlul exact.
    """
    return book_summaries_dict.get(title, "Rezumat indisponibil pentru acest titlu.")
