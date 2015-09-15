.. _Mathematische Beschreibung einer harmonischen Schwingung:

Exkurs: Mathematische Beschreibung einer harmonischen Schwingung
================================================================

Die mathematische Beschreibung eines harmonisch schwingenden Gegenstands
("Oszillators") wird häufig als Basis-Modell in der theoretischen Physik
genutzt. In diesem Abschnitt wird daher das grundlegende mathematische Konzept
für Interessierte kurz vorgestellt.

Ein Körper führt genau dann eine harmonische Schwingung aus, wenn auf ihn eine
eine Kraft wirkt, die proportional zu seiner Auslenkung ist und stets in
Richtung der Ruhelage zeigt; die Dämpfung der Schwingung sollte vernachlässigbar
gering ist.


.. index:: Federpendel
.. _Federpendel:

Das Federpendel
---------------

In guter Näherung werden diese Bedingungen von einem Pendelkörper, der an einer
hängenden Schraubenfeder befestigt ist, erfüllt. Bei einer Auslenkung :math:`s`
aus der Ruhelage ist die rücktreibende Kraft gleich der Spannkraft :math:`F
_{\rm{S}}` der Schraubenfeder. Diese hängt von der Federhärte :math:`D` ab und
ist der Auslenkung entgegengesetzt:

.. math::

    F = - D \cdot s

Die Kraft ruft im schwingenden Gegenstand eine Beschleunigung :math:`a` hervor,
die nach dem Kraftgesetz als :math:`F = m \cdot a` beschrieben werden kann,
wobei :math:`m` die Masse des Oszillators symbolisiert. Die Beschleunigung
:math:`a` entspricht nun gerade der zeitlichen Änderung der Geschwindigkeit,
welche wiederum einer zeitlichen Änderung des Ortes bzw. der Auslenkung
entspricht.

Aus mathematischer Sicht sind die zur Auslenkung :math:`s` proportionale Kraft
und ihre zur Beschleunigung :math:`a = \dot{v} = \ddot{s}` proportionale Wirkung
über eine zweifache zeitliche Ableitung miteinander gekoppelt. Es gilt somit:

.. math::

    m \cdot \ddot{s} = - D \cdot s

Diese Gleichung kann so umsortiert werden, dass beide von der Auslenkung
:math:`s` abhängigen Größen auf der linken Seite stehen:

.. math::

    m \cdot \ddot{s} + D \cdot s = 0

Noch deutlicher wird der Charakter dieser "Differentialgleichung", wenn man die
Gleichung durch die Masse :math:`(m \ne 0)` teilt:

.. math::
    :label: eqn-harmonischer-oszillator

    \ddot{s} + \frac{D}{m} \cdot s = 0

Diese Gleichung wird von jeder zeitabhängigen Funktion :math:`s(t)` erfüllt,
deren zweite zeitliche Ableitung der ursprünglichen Funktion bis auf einen
konstanten Faktor identisch ist. Eine bekannte Funktion, die diese Bedingung
erfüllt, ist die Sinus-Funktion. Ein Ansatz für den zeitlichen Verlauf der
Auslenkung :math:`s`  kann somit folgendermaßen lauten:

.. math::
    :label: eqn-harmonischer-oszillator-ansatz

    s = \sin{(\omega \cdot t)}

Dabei gibt :math:`\omega` die so genannte "Oszillator-Frequenz" an. Sie erinnert
an die :ref:`Winkelgeschwindigkeit <Winkelgeschwindigkeit>` einer kreisförmigen
Bewegung, denn multipliziert mit der Zeit :math:`t` beschreibt sie den Ort, an
dem sich der periodisch schwingende Körper gerade befindet. [#]_

Bildet man für den Ansatz :eq:`eqn-harmonischer-oszillator-ansatz` :math:`s` die
erste und zweite zeitliche Ableitung der Sinusfunktion, so erhält man unter
Berücksichtigung der :ref:`Kettenregel <gwm:Allgemeine Ableitungsregeln>`:

.. math::

    \dot{s} &= \phantom{+} \omega \cdot \cos{(\omega \cdot t)} \\[10pt]
    \ddot{s} &= - \omega ^2 \cdot \sin{(\omega \cdot t)}

Die zweite zeitliche Ableitung :math:`\ddot{s}` ist somit mit der ursprünglichen
Sinus-Funktion :eq:`eqn-harmonischer-oszillator-ansatz`, welche die Auslenkung
:math:`s` beschreibt, bis auf einen Faktor :math:`- \omega ^2` identisch:

.. math::

    \ddot{s} = - \omega ^2 \cdot s

Dieses Ergebnis kann direkt in Gleichung :eq:`eqn-harmonischer-oszillator`
eingesetzt werden. Es folgt:

.. math::

    - \omega ^2 \cdot s + \frac{D}{m} \cdot s = 0

Auf der linken Seite kann :math:`s` ausgeklammert werden. Es ergibt sich:

.. math::

    \left( - \omega ^2 + \frac{D}{m} \right) \cdot s = 0

Diese Gleichung ist einerseits erfüllt, wenn :math:`s = 0` gilt, d.h. der
Körper sich in der Ruhelage befindet. Andererseits gilt das Gleichheitszeichen
für jede beliebige Auslenkung, wenn der eingeklammerte Ausdruck als ganzes
gleich Null ist. Somit gilt:

.. math::

   -  \omega ^2 +  \frac{D}{m} = 0

und damit:

.. math::
    :label: eqn-oszillator-frequenz

    \omega ^2 = \frac{D}{m} \quad \Leftrightarrow \quad \omega = \sqrt{\frac{D}{m} }

Die Oszillator-Frequenz des schwingenden Pendelkörpers ist somit umso größer,
desto größer die Federkonstante ("Härte") :math:`D` der Schraubenfeder ist.
Andererseits schwingt der Oszillator umso schneller, desto geringer seine Masse
:math:`m` ist.

.. Schwingungsdauer:

.. Aus :math:`D^2 = m \cdot \omega^2 = \frac{4 \cdot \pi^2}{T^2}` erhält man
.. T = 2 \cdot \pi \cdot \sqrt{\frac{m}{D}}

Die Weg-Zeit-Funktion :math:`s = \sin{(\omega \cdot t)}` kann auch graphisch
als Diagramm dargestellt werden. Es ergibt sich der für harmonische
Schwingungen typische sinusförmige Verlauf. Je schneller der Pendelkörper
schwingt, desto schmäler werden die "Berge und Täler" der Sinus-Kurve; je
größer die maximale Auslenkung ist, desto höher bzw. tiefer liegen die Hoch-
und Tiefpunkte.

Die Sinus-Funktion eignet sich als Ansatz, wenn der Pendelkörper zu Beginn in
der Ruhelage ist und in dieser Position von außen "angestoßen" wird. Ist der
maximal ausgelenkt und wird von dieser Position aus losgelassen, so ist die
Kosinus-Funktion als Ansatz besser geeignet.

Die oben hergeleiteten Ergebnisse lassen sich beispielsweise auch auf die
Schwingungen eines gefederten Fahrzeugs oder einer gefedert gelagerten Maschine
(z.B. Waschmaschine) übertragen.

.. index:: Fadenpendel, Mathematisches Pendel
.. _Fadenpendel:

Das Fadenpendel
---------------

Auch Schwingungen eines Fadenpendels haben -- bei nicht zu großer Auslenkung des
Pendelkörpers -- annähernd einen sinusförmigen Verlauf. Ist die Masse des Fadens
vernachlässigbar klein und die Größe des Pendelkörpers klein im Vergleich zur
Fadenlänge, so spricht man von einem mathematischen Pendel.

.. figure:: ../../pics/mechanik/schwingungen-und-wellen/fadenpendel.png
    :name: fig-fadenpendel
    :alt:  fig-fadenpendel
    :align: center
    :width: 35%

    Schematischer Aufbau eines Fadenpendels.

    .. only:: html

        :download:`SVG: Fadenpendel
        <../../pics/mechanik/schwingungen-und-wellen/fadenpendel.svg>`

Die rücktreibend wirkende Kraft einer Pendelschwingung lässt sich bestimmen,
indem man die Gewichtskraft :math:`F _{\rm{G}}` des Pendelkörpers in zwei
:ref:`Teilkräfte <Zerlegung einer Kraft in Teilkräfte>` (längs und quer zur
Schwingungsrichtung) zerlegt: Die Teilkraft :math:`F _{\rm{S}}` in Seilrichtung
hält den Faden gespannt, die Teilkraft :math:`F _{\rm{R}}` in
Schwingungsrichtung entspricht der rücktreibenden Kraft. Ist der
Auslenkungswinkel :math:`\varphi` klein, so ist die Länge :math:`s ^{*}` des
Kreisbogens näherungsweise gleich dem waagrechten Abstand :math:`s` des
Pendelkörpers von der Ruhelage. [#]_

.. index:: Richtgröße

Für die rücktreibende Kraft :math:`F _{\rm{R}}` gilt mit :math:`\sin{(\varphi)}
= \frac{s}{l}`:

.. math::

    F _{\rm{R}} &= F _{\rm{G}} \cdot \sin{(\varphi)} = m \cdot g \cdot \frac{s}{l}
    = \frac{m \cdot g}{l} \cdot s

Der Term :math:`\frac{m \cdot g}{l}` hat somit die gleiche Bedeutung für das
Fadenpendel wie die Federhärte :math:`D` für das Federpendel. Man bezeichnet
ihn daher auch als "Richtgröße" :math:`D` eines mathematischen Pendels.

Für die Oszillatorfrequenz eines mathematischen Pendels gilt nach Gleichung
:eq:`eqn-oszillator-frequenz`:

.. math::
    :label: eqn-oszillator-frequenz-fadenpendel

    \omega = \sqrt{\frac{D}{m}} = \sqrt{\frac{g}{l}}

Experimentell bestätigt sich, dass die Schwingungsfrequenz eines Fadenpendels
zwar von der Länge :math:`l` des Pendels, aber nicht von der Masse des
Pendelkörpers abhängig ist. Bei kleinen Auslenkungen :math:`(\varphi < 10
\degree)` ist die Frequenz bzw. Schwingungsdauer zudem unabhängig von der
Amplitude.

Pendel, bei denen die obigen Bedingungen erfüllt sind, nennt man Fadenpendel
oder auch mathematische Pendel. Im Gegensatz dazu bezeichnet man beliebige,
drehbar aufgehängte Gegenstände als physikalische Pendel.


.. index:: Physikalisches Pendel
.. _Physikalisches Pendel:

Das physikalische Pendel
------------------------

Führt ein beliebiges, drehbar gelagertes Objekt Schwingungsbewegungen aus, so
können diese bei nur kleinen Auslenkungen und bei Vernachlässigung des
Luftwiderstands ebenfalls als harmonische Schwingungen beschrieben werden.

.. figure:: ../../pics/mechanik/schwingungen-und-wellen/physikalisches-pendel.png
    :name: fig-physikalisches-pendel
    :alt:  fig-physikalisches-pendel
    :align: center
    :width: 35%

    Schematischer Aufbau eines Physikalischen Pendels.

    .. only:: html

        :download:`SVG: Physikalisches Pendel
        <../../pics/mechanik/schwingungen-und-wellen/physikalisches-pendel.svg>`

Die rücktreibende Größe ist in diesem Fall das Drehmoment :math:`\vec{M} =
\vec{s} \times \vec{F} _{\rm{G}}` des Körperschwerpunkts bezüglich der Drehachse;
dabei bezeichnet :math:`s` den horizontalen Abstand des Schwerpunkts von der
Ruhelage. Bei einem kleinen Auslenkungswinkel :math:`\varphi` kann für den
Betrag des Drehmoments folgendes geschrieben werden:

.. math::

    M = - s \cdot F _{\rm{G}} = - s \cdot m \cdot g \approx  - (l \cdot \varphi) \cdot
    m \cdot g = - l \cdot m \cdot g \cdot \varphi

Hierbei wurde die Näherung :math:`s = l \cdot \sin{(\varphi)} \approx l \cdot
\varphi` verwendet; das negative Vorzeichen berücksichtigt die Auslenkung in
negative :math:`x`-Richtung. Für das Drehmoment :math:`M` gilt allerdings
ebenso folgender Zusammenhang:

.. math::

    M = J \cdot \alpha = J \cdot \ddot{\varphi}

Hierbei steht :math:`J` für das :ref:`Trägheitsmoment <Trägheitsmoment>` des
schwingenden Gegenstands und :math:`\alpha = \ddot{\varphi}` für die
:ref:`Winkelbeschleunigung <Kreisförmige Bewegung mit konstanter
Beschleunigung>`. Setzt man beide Terme gleich, erhält man folgende
Differentialgleichung:

.. math::

    J \cdot \ddot{\varphi} = -(m \cdot g \cdot l) \cdot \varphi

Wählt man als Lösung der Differentialgleichung wiederum :math:`\varphi =
\sin{(\omega \cdot t)}`, so gilt wegen :math:`\ddot{\varphi} = -\omega^2 \cdot
\sin{(\omega \cdot t)} = - \omega^2 \cdot \varphi`:

.. math::

    - J \cdot \omega^2 \cdot \varphi = -(m \cdot g \cdot l) \cdot \varphi

Für :math:`\varphi \ne 0` ergibt sich damit für die Oszillator-Frequenz
:math:`\omega` eines physikalischen Pendels:

.. math::
    :label: eqn-oszillator-frequenz-physikalisches-pendel

    J \cdot \omega ^2 = m \cdot g \cdot l \quad \Leftrightarrow \quad \omega =
    \sqrt{\frac{m \cdot g \cdot l}{J}}

Die Oszillator-Frequenz :math:`\omega` eines physikalischen Pendels hängt somit
von der Masse des schwingenden Objekts, der Lage seines Schwerpunkts sowie von
seinem Trägheitsmoment ab. Bei dieser Frequenz sind ebenfalls :ref:`Resonanz
<Erzwungene Schwingungen und Resonanz>`-Effekte am stärksten ausgeprägt.



..
    Bei Flüssigkeitsschwingungen, beispielsweise einem U-Rohr, ist nur die
    Länge der Flüssigkeitssäule von Bedeutung. Die Art der Flüssigkeit, die
    Querschnittsfläche des U-Rohrs und die unterschiedlichen
    Flüssigkeitshöhen auf beiden Seiten haben keinen Einfluss.
    Auch: Hahn S.367

    In der Ruhelage haben die Flüssigkeitssäulen in den Schenkeln eines U-Rohres
    nach Bild 5.4 gleiche Höhe. Drückt man die eine Säule um ein Stück x tiefer, so
    steigt die andere um den gleichen Betrag, falls die Querschnitte A in beiden
    Schenkeln gleich sind. Die Höhendifferenz ist dann 2 \cdot x, der Druck p =
    2\cdot x \cdot \rho \cdot g (\rho = Dichte), die rückstellende Kraft also

    .. math::

        F = - p \cdot A = - 2 \cdot A \cdot \rho \cdot x

    Minuszeichen, weil x und F entgegengesetzte Richtungen haben. Es liegt also ein
    lineares Kraftgesetz vor. Das bedeutet: Die Flüssigkeit in einem
    kommunizierenden Rohrsystem mit konstanten Querschnitten kann sinusförmige
    Schwingungen ausführen.

    Setzt man die Richtgröße von D = 2 \cdot A \cdot  g ein, so erhält man T_0 = 2
    \cdot \pi \cdot \sqrt{m/(2 \cdot A \cdot \rho \cdot p)}, oder mit \rho = m/V und
    (bei konstantem Querschnitt A) = A \cdot l (Bild 5.4))
    T_0 = 2 \cdot \pi \cdot \sqrt{ l/(2g)}.

    Dieser Modellfall lässt sich auf beliebig geformte flüssigkeitsgefüllte Gefäße
    verallgemeinern, allerdings sind dann die Schwingungen im Allgemeinen nicht mehr
    sinusförmig.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Bisweilen wird die Oszillator-Frequenz deshalb auch "Kreisfrequenz"
    genannt. Sie gibt an, welche Winkelgeschwindigkeit ein Punkt einer
    rotierenden Kreisscheibe haben müsste, damit seine Frequenz mit derjenigen
    des schwingenden Pendelkörpers übereinstimmt.

    Da die Schwingungsfrequenz :math:`f` des Pendels die Anzahl an
    Schwingungsvorgängen je Sekunde angibt, und für eine ganze Umdrehung der
    Kreisscheibe ein Winkel von :math:`2 \cdot \pi` nötig ist, muss die
    Kreisfrequenz :math:`\omega` (gemessen in Rad je Sekunde) um genau diesen
    Faktor größer sein als die Frequenz :math:`f`:

    .. math::

        \omega = 2 \cdot \pi \cdot f

.. [#] Für den Auslenkungswinkel sollte :math:`\varphi < 10 \degree` gelten;
    dann beträgt der relative Fehler :math:`\frac{s}{s ^{*}}` zwischen dem
    waagrechten Abstand :math:`s = l \cdot \sin{(\varphi)}` und der Länge des
    entsprechenden Kreisbogens :math:`s ^{*} = \frac{\varphi}{360 \degree} \cdot
    2 \cdot \pi \cdot l` weniger als :math:`0,5\%`.


