.. _Elektrische Felder:

Elektrische Felder
==================

In ähnlicher Weise wie man das magnetische Feld eines Permanent- oder
Elektromagneten zur Beschreibung der Kraftwirkung auf einen anderen Magneten
nutzen kann, ist es auch möglich, das elektrische Feld einer Ladungsverteilung
zur Beschreibung der Kraftwirkung auf andere elektrische Ladungen zu verwenden.
Anders als Magnetfelder verlaufen elektrische Felder jedoch nicht auf
geschlossenen Linien, sondern verlaufen von positiven elektrischen Ladungen hin
zu negativen Ladungen.


.. index:: Coulomb-Kraft
.. _Coulomb-Kraft:

.. rubric:: Das Coulombsche Kraftgesetz

Die Grundlage für die Einführung eines elektrischen Felds bildet das so
genannte `Colulomb
<https://de.wikipedia.org/wiki/Charles_Augustin_de_Coulomb>`_-Gesetz, das
besagt, dass die Kraft zwischen zwei punktförmigen Ladungen proportional zu
Ladungsmengen :math:`Q_1` und :math:`Q_2` sowie indirekt proportional zum
Quadrat des Abstands :math:`r` beider Ladungen ist:

.. math::
    :label: eqn-coulomb
    
    F _{\rm{el}} = \frac{1}{4 \cdot \pi \cdot \varepsilon _0} \cdot \frac{Q_1
    \cdot Q_2}{r^2}

Hierbei ist :math:`\varepsilon _0 = \unit[8,854 \cdot 10 ^{-12}]{\frac{A \cdot
s}{V \cdot m}}` die elektrische Feldkonstante des Vakuums. Die Einheit dieser
wichtigen Naturkonstanten kann wegen :math:`\unit[1]{V} = \unit[1]{\frac{J}{C}}
=` auch folgendermaßen geschrieben werden:

.. math::
    
    \unit{\frac{V \cdot m}{A \cdot s}} = \unit{\frac{V \cdot m}{C}} =
    \unit{\frac{J \cdot m}{C^2}} = \unit{\frac{N \cdot m^2}{C^2}}

Mit Hilfe der elektrischen Feldkonstanten kann bei bekannten Ladungsmengen und
ihrem Abstand auf die Größe der wirkenden Kraft geschlossen werden; der gesamte
Vorfaktor :math:`\frac{1}{4 \cdot \pi \cdot \varepsilon_0} \approx \unit[8,99
\cdot 10^9]{\frac{N \cdot m^2}{C^2}}` wird bisweilen auch als
"Coulomb-Konstante" bezeichnet. Anschaulich bedeutet der Wert dieser Konstante,
dass zwei Ladungen von je einem Coulomb, die sich in einem Abstand von einem
Meter zueinander befinden, aufeinander eine Kraft von etwa :math:`\unit[9]{GN}`
ausüben würden -- das entspräche einer Gewichtskraft von etwa :math:`\unit[10
^6]{Tonnen}`. Man erkennt an diesem Beispiel zum einen, dass bei vielen
Prozessen, etwa bei sich bewegenden Elektronen, die Gewichtskraft gegenüber der
Coulomb-Kraft meist völlig vernachlässigt werden kann. Andererseits zeigt sich,
dass 1 Coulomb eine sehr große Ladungsmenge darstellt; im Alltag treten 
üblicherweise nur Bruchteile dieser Ladungsmenge auf.

Für die Richtung der wirkenden Coulomb-Kraft gilt:

* Sind die Vorzeichen beider Ladungen gleich, so ist die wirkende Kraft positiv,
  und die Ladungen stoßen sich ab. 
* Haben beide Ladungen hingegen unterschiedliche Vorzeichen, so ist die
  Coulomb-Kraft negativ, und die Ladungen ziehen einander an. 

Sind mehrere Ladungen räumlich getrennt angeordnet, so kann man zunächst die
Coulomb-Kräfte paarweise berechnen und anschließend die wirkenden
Gesamt-Kräfte durch Addition der Teilkräfte ermitteln.


.. index:: Elektrische Feldstärke, Feldlinien (elektrisch)
.. _Elektrische Feldstärke:

Die elektrische Feldstärke
--------------------------

Liegt eine kontinuierliche Verteilung vieler einzelner Ladungen vor, so wäre es
zumindest sehr mühsam, die resultierende Wirkung auf eine weitere Probeladung
als Überlagerung der zahlreichen einzelnen Coulomb-Kräfte zu beschreiben.
Stattdessen verwendet man den Begriff der elektrischen Feldstärke
:math:`\vec{E}`; diese gibt an, welche Kraftwirkung :math:`\vec{F}` eine
Probeladung :math:`Q _{\rm{p}}` durch eine bereits vorhandene Ladung oder
Ladungsverteilung erfährt:

.. math::
    
    \vec{E} = \frac{\vec{F} _{\rm{el}}}{Q _{\rm{p}}}

Die elektrische Feldstärke wird in der Einheit :math:`\unit{\frac{N}{C}}`
angegeben. [#]_ Als Vektor gibt die elektrische Feldstärke die Richtung der Kraft an,
die auf eine positive Probeladung wirkt. Die einzelnen Feldlinien gehen deshalb
senkrecht von positiven Ladungen aus und enden senkrecht auf negativen Ladungen.
Die Dichte der Feldlinien kann dabei als Maß für die Stärke des elektrischen
Felds angesehen werden.

.. figure::
    ../pics/elektrizitaet-magnetismus/feldlinien-elektrische-ladungen.png
    :width: 50%
    :align: center
    :name: fig-feldlinien-elektrische-ladungen
    :alt:  fig-feldlinien-elektrische-ladungen

    Feldlinien von unterschiedlichen und gleichen elektrischen Ladungen gleicher
    Ladungsmenge.

    .. only:: html
    
        :download:`SVG: Feldlinien einzelner elektrischer Ladungen
        <../pics/elektrizitaet-magnetismus/feldlinien-elektrische-ladungen.svg>`

Die Kraftwirkung auf negative Probeladungen ergibt sich, indem man sich die
Pfeilrichtung der Feldlinien vertauscht vorstellt.

.. index:: Plattenkondensator
.. _Plattenkondensator:

Das elektrische Feld eines Plattenkondensators
----------------------------------------------

Ein elektrisches Feld mit gleichmäßig verteilten und in die gleiche Richtung
zeigenden Feldlinien erhält man, wenn man zwei metallische, zueinander parallel
angeordnete Platten mit entgegengesetzten Ladungsträgern bestückt. Im Inneren
eines solchen "Plattenkondensators" ist die elektrische Feldstärke an allen
stellen gleich ("homogen"). [#]_

.. figure::
    ../pics/elektrizitaet-magnetismus/plattenkondensator.png
    :width: 50%
    :align: center
    :name: fig-plattenkondensator
    :alt:  fig-plattenkondensator

    Das elektrische Feld im Inneren eines Plattenkondensators.

    .. only:: html
    
        :download:`SVG: Plattenkondensator
        <../pics/elektrizitaet-magnetismus/plattenkondensator.svg>`


.. index:: Elektrische Flussdichte

Der Betrag der elektrischen Feldstärke eines Plattenkondensators ist davon
abhängig, wie viele zusätzliche Ladungen sich über den Plattenflächen
befinden. Das Verhältnis aus der gespeicherten Ladungsmenge :math:`Q` und der
Plattenfläche :math:`A` wird auch als "elektrische Flussdichte" :math:`\vec{D}`
bezeichnet. Für ihren Betrag gilt:

.. math::
    :label: eqn-elektrische-flussdichte
    
    D = \frac{Q}{A}

Die elektrische Flussdichte :math:`\vec{D}` steht, wie auch die elektrische
Feldstärke :math:`\vec{E}`, senkrecht zu den Kondensatorplatten. Der
Zusammenhang zwischen der elektrischen Flussdichte :math:`D`, welche die
Ladungsverteilung beschreibt, und der elektrischen Feldstärke :math:`\vec{E}`,
welche die Kraftwirkung auf geladene Teilchen angibt, kann wiederum mittels der
elektrischen Feldkonstante :math:`\varepsilon _0` formuliert werden:

.. math::
    :label: eqn-elektrische-flussdichte-und-feldstaerke
    
    D = \varepsilon_0 \cdot E \quad \Leftrightarrow \quad E =
    \frac{1}{\varepsilon_0} \cdot D = \frac{1}{\varepsilon_0} \cdot \frac{Q}{A}

Um einen noch einfacheren Ausdruck für die Elektrische Feldstärke herzuleiten,
ist ein kurzes Gedankenexperiment hilfreich: Wird ein einzelne positive
Probeladung :math:`Q _{\rm{p}}` entgegen den Feldlinien von der negativen zur
positiv geladenen Platte verschoben, so muss dafür eine Arbeit :math:`W = F
_{\rm{el}} \cdot d = Q _{\rm{p}}\cdot E \cdot d` verrichtet werden, wobei
:math:`d` den Plattenabstand bezeichnet. Befindet sich die Ladung anschließend
an der positiven Seite, so besitzt sie eine ebenso große potentielle Energie
:math:`E _{\rm{pot}}`. Als elektrische Spannung :math:`U` bezeichnet man eben
diese potentielle Energie, bezogen auf die Größe :math:`Q _{\rm{p}}` der
Probeladung:

.. math::
    
    U = \frac{E _{\rm{pot}}}{Q _{\rm{p}}} 

Setzt man :math:`E _{\rm{pot}} = Q _{\rm{p}} \cdot E \cdot d` in die obige
Formel ein, so ergibt sich für das elektrische Feld :math:`E` eines
Plattenkondensators folgender nützlicher Zusammenhang:

.. math::
    :label: eqn-elektrische-feldstaerke-plattenkondensator
    
    U = E \cdot d \quad \Leftrightarrow \quad E = \frac{U}{d}

Da sowohl die elektrische Spannung :math:`U` als auch der Abstand :math:`d`
zwischen den geladenen Platten leicht messbare Größen sind, kann das elektrische
Feld eines Plattenkondensators sehr einfach bestimmt werden.

Während das elektrische Feld an allen Stellen im Plattenkondensator gleich ist,
nimmt die elektrische Spannung im Kondensator von der positiven zur negativen
Platte linear auf Null ab.


.. index:: Elektrische Influenz, Influenz
.. _Elektrische Influenz:

Elektrische Influenz und Faradayischer Käfig
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Metallen gibt es stets eine Vielzahl an frei beweglicher Elektronen. Im
neutralen Zustand werden die negativen Ladungen der Elektronen durch die
positiven Ladungen der Atomrümpfe ausgeglichen. Lädt man ein einzelnes Stück
Metall mit weiteren Elektronen auf, so verteilen sich diese ausschließlich
entlang der Oberfläche, da die zusätzlichen Elektronen ebenfalls frei
beweglich sind und sich gegenseitig abstoßen.

.. index:: Faradayischer Käfig

Bringt am ein Stück Metall in ein elektrisches Feld ein, so bewirkt dieses eine
Verschiebung der frei beweglichen Elektronen zur positiven Platte hin; an der
zur negativen Platte hin orientierten Seite bleiben die positiv geladenen
Atomrümpfe übrig. Dieser als "elektrische Influenz" bezeichnete Effekt hält so lange an,
bis sich im Metall durch die Ladungsverschiebung ein gleich starkes, aber
entgegengesetzt gerichtetes Feld einstellt.

.. figure::
    ../pics/elektrizitaet-magnetismus/plattenkondensator-influenz.png
    :width: 50%
    :align: center
    :name: fig-plattenkondensator-influenz
    :alt:  fig-plattenkondensator-influenz

    Elektrische Influenz im Feld eines Plattenkondensators.

    .. only:: html
    
        :download:`SVG: Elektrische Influenz
        <../pics/elektrizitaet-magnetismus/plattenkondensator-influenz.svg>`


Im Inneren des Metalls überlagern sich das äußere und das induzierte
elektrische Feld. Da beide Felder gleich groß, aber entgegengesetzt gerichtet
sind, bleibt das Innere des Metalls somit feldfrei. Dies gilt nicht nur massive
metallische Körper, sondern auch für metallische Hohlkörper. In der Technik
stellen beispielsweise Autokarosserien so genannte "Faradayische Käfige" dar,
welche die Insassen vor elektrischen Feldern und damit auch vor Stromflüssen,
beispielsweise Blitzen, schützen. [#]_

.. index:: Orientierungspolarisation, Elektrischer Dipol
.. _Orientierungspolarisation:

Orientierungspolarisation
^^^^^^^^^^^^^^^^^^^^^^^^^

Befinden sich zwei Ladungen mit unterschiedlichem Vorzeichen, aber gleich
großer Ladungsmenge :math:`Q` im Abstand :math:`l` zueinander, so spricht man
von einem elektrischen Dipol. Ein solcher Dipol besitzt ein so genanntes
Dipolmoment :math:`\vec{p}`, das proportional zur Ladungsmenge und zum Abstand
der Ladungen ist und in Richtung der positiven Ladung zeigt: 

.. math::
    
    \vec{p} = Q \cdot \vec{l}

Die Einheit des Dipolmoments ist :math:`\unit{C \cdot m}`.

.. immer noch gebräuchlich: Einheit Debye

.. figure::
    ../pics/elektrizitaet-magnetismus/elektrischer-dipol.png
    :width: 50%
    :align: center
    :name: fig-elektrischer-dipol
    :alt:  fig-elektrischer-dipol

    Prinzip eines elektrischen Dipols.

    .. only:: html
    
        :download:`SVG: Elektrischer Dipol
        <../pics/elektrizitaet-magnetismus/elektrischer-dipol.svg>`

In der Realität existieren elektrische Dipole in Form von bestimmten Molekülen,
die ein permanentes Dipolmoment besitzen, beispielsweise Wasser. 

Bringt man einen elektrischen Dipol in ein homogenes elektrisches Feld ein, so
richtet er sich parallel zur Feldrichtung aus. Für das dabei wirkende
:ref:`Drehmoment <Drehmoment>` :math:`\vec{M}` gilt: 

.. math::
    
    \vec{M} = \vec{l} \times \vec{F} = Q \cdot \vec{l} \times \frac{\vec{F}}{Q}
    = \vec{p} \times \vec{E}

Das Drehmoment ist maximal, wenn der elektrische Dipol senkrecht zu den
elektrischen Feldlinien ausgerichtet ist, und wird gleich Null, wenn beide
Richtungen identisch sind.

Die Ausrichtung von elektrischen Dipolen durch elektrische Felder wird als
Orientierungspolarisation bezeichnet. In realen Anwendungen verhindert die
statistisch gleichmäßig verteilte Wärmebewegung der Teilchen eine vollständig
Ausrichtung der Dipole; bei abnehmender Temperatur nimmt die
Orientierungspolarisation daher zu. Bei Abschalten des elektrischen Felds
verschwindet die Orientierungspolarisation wieder.


.. index:: Verschiebunspolarisation, Dielektrikum
.. _Dielektrikum:

Verschiebunspolarisation und Dielektrikum
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bringt man ein nichtleitendes Material ("Dielektrikum") ohne elektrische Dipole
in ein homogenes elektrisches Feld ein, so werden die Ladungsschwerpunkte in
allen Atomen leicht verschoben, jeder Atomkern gerät etwas aus dem Zentrum
seiner Elektronenhülle. Alle Atome werden somit zu elektrischen Dipolen, auch
wenn sie ursprünglich keinen Dipolcharakter besessen haben. Diese Form der
Polarisation wird Verschiebungspolarisation genannt.

.. figure::
    ../pics/elektrizitaet-magnetismus/plattenkondensator-polarisation.png
    :width: 50%
    :align: center
    :name: fig-plattenkondensator-polarisation
    :alt:  fig-plattenkondensator-polarisation

    Elektrische Polarisation im Feld eines Plattenkondensators.

    .. only:: html
    
        :download:`SVG: Elektrische Polarisation
        <../pics/elektrizitaet-magnetismus/plattenkondensator-polarisation.svg>`

Bei beiden Polarisationsformen erzeugen die Dipole im Dielektrikum selbst ein
vergleichsweise schwaches und dem äußeren Feld entgegengesetzt gerichtetes
elektrisches Feld. Füllt das Dielektrikum den gesamten Bereich zwischen den
Kondensatorplatten aus, so wird der Wert der elektrischen Feldstärke
:math:`\vec{E}` gegenüber dem ursprünglichen Wert um einen Faktor
:math:`\varepsilon _{\rm{r}}` gesenkt. Für einen Plattenkondensator mit
Dielektrikum gilt also allgemein: 

.. math::
    
    E = \frac{1}{\varepsilon _{\rm{r}} \cdot \varepsilon _0} \cdot \frac{Q}{A} =
    \frac{1}{\varepsilon _{\rm{r}}} \cdot \frac{U}{d}


.. _Dielektrizitätszahl:

Der Zahlenwert :math:`\varepsilon _{\rm{r}}` ist eine Materialkonstante, die als
relative Dielektrizitätszahl bezeichnet wird. Streng genommen muss bereits Luft
als Dielektrikum angesehen werden, ihr Wert ist jedoch nur geringfügig von der
Dielektrizitätszahl des Vakuums.

.. list-table:: 
    :name: tab-dielektrizitaetszahlen
    :widths: 50 50 

    * - Material
      - Dielektrizitätszahl :math:`\varepsilon _{\rm{r}}`
    * - Erde (feucht)
      - :math:`29`
    * - Erde (trocken)
      - :math:`3,9`
    * - Glas
      - :math:`6` bis :math:`8`
    * - Glimmer
      - :math:`5,4`
    * - Gummi
      - :math:`3`
    * - Glycerin
      - :math:`24,5`
    * - Holz (trocken)
      - :math:`2` bis :math:`3,5`
    * - Luft
      - :math:`1,00059`
    * - Porzellan
      - :math:`2` bis :math:`6`
    * - Wasser
      - :math:`80`

Wird ein Kondensator durch eine an die Platten angeschlossene Stromquelle
aufgeladen, so erfolgt dies so lange, bis die Spannung :math:`U` im Kondensator
genauso groß ist wie die anliegende äußere Spannung. Durch ein Einbringen eines
Dielektrikum wird allerdings das elektrische Feld und somit auch die Spannung im
Kondensator gesenkt; somit fließt weitere Ladung auf die Kondensatorplatten
nach, bis erneut die Spannung im Kondensator (mit Dielektrikum) so groß ist wie
die anliegende Spannung. Ein Plattenkondensator kann also mit Dielektrikum eine
größere Ladungsmenge speichern als ohne.


.. index:: Kapazität
.. _Die Kapazität eines Plattenkondensators:

Die Kapazität eines Plattenkondensators
---------------------------------------

Die Kapazität eines Plattenkondensators gibt an, wie viel die Ladungsmenge
:math:`Q` ist, die der Kondensator bei einer anliegenden Spannung :math:`U`
insgesamt aufnehmen kann:

.. math::
    :label: eqn-kapazitaet
    
    C = \frac{Q}{U}

Die Einheit der Kapazität ist Farad :math:`(\unit[1]{F} =
\frac{\unit[1]{C}}{\unit[1]{V}})`. Da ein Coulomb eine sehr große Ladungsmenge
darstellt, ist ebenso eine Kapazitätsmenge von einem Farad sehr groß. In der
Praxis übliche Kondensatoren werden daher in Pikofarad :math:`(\unit{pF})`,
:math:`(\unit{nF})` oder Mikrofarad :math:`(\unit{\mu F})` angegeben.

Die obige Formel :eq:`eqn-kapazitaet` gilt allgemein für alle Bauarten von
Kondensatoren. Bei einem Plattenkondensator ist die Kapazität abhängig
von der Fläche :math:`A` der beiden Kondensatorplatten, von ihrem Abstand
:math:`d` sowie vom Dielektrikum, das sich zwischen den beiden
Kondensatorplatten befindet. Handelt es sich beim Dielektrikum um Vakuum oder
Luft, so gilt für die Kapazität :math:`C` des Plattenkondensators:

.. math::
    :label: eqn-kapazitaet-plattenkondensator
    
    C = \varepsilon _0 \cdot \frac{A}{d} 

Hierbei bezeichnet :math:`\varepsilon _0= \unit[8,854 \cdot 10 ^{-12}]{\frac{A
\cdot s}{V \cdot m}}` wiederum die elektrische Feldkonstante. Handelt es sich
beim Dielektrikum um ein anderes Material, so muss anstelle von
:math:`\varepsilon _0` der Wert :math:`\varepsilon = \varepsilon _{\rm{r}} \cdot
\varepsilon _0` in die obige Gleichung eingesetzt werden, wobei
:math:`\varepsilon _{\rm{r}}` die :ref:`Dielektrizitätszahl
<Dielektrizitätszahl>` des jeweiligen Materials ist. Durch ein geeignetes
Dielektrikum zwischen den Kondensatorplatten kann somit die Kapazität des
Kondensators bei gleicher Baugröße um ein Vielfaches erhöht werden.



.. Bewegung von Teilchen in elektrischen Feldern

.. Q * U = e * U = Energie = 1/2 m v^2



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Eine weitere gebräuchliche Einheit für die elektrische Feldstärke ist
    :math:`\unit{\frac{V}{m}}`. Der Zusammenhang ergibt sich aus der Definition von der
    Einheit Volt:

    .. math::
        
        \unit{V} = \unit{\frac{J}{C}} = \unit{\frac{N \cdot m}{C}}

    Damit lässt sich die Einheit der elektrischen Feldsterke folgendermaßen
    umformulieren:

    .. math::
        
        \unit{\frac{N}{C}} = \unit{\frac{N \cdot m}{C \cdot m}} = \unit{\frac{V}{m}} \quad
        \checkmark

.. [#] An den Rendern des Kondensators sind die Feldlinien zwar gekrümmt, doch
    im Inneren verlaufen die Feldlinien nahezu parallel.

.. [#] Der Faradayische Kaefig ist nach dem Physiker `Michael Faraday
    <https://de.wikipedia.org/wiki/Michael_Faraday>`_ benannt.
