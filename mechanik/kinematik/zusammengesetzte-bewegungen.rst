.. _Zusammengesetzte Bewegungen:

Zusammengesetzte Bewegungen
===========================

Körper bewegen sich häufig nicht geradlinig in eine einzige Richtung, sondern
gleichzeitig in zwei oder drei Raumrichtungen. Hierbei können die Bewegungen in
die einzelnen Raumrichtungen getrennt betrachtet werden.


.. _Überlagerung zweier Bewegungen mit konstanter Geschwindigkeit:

Überlagerung zweier Bewegungen mit konstanter Geschwindigkeit
-------------------------------------------------------------

Verlaufen zwei Bewegungen geradlinig entlang einer gemeinsamen Linie, so genügt
eine einfache Addition der beiden Geschwindigkeitsbeträge :math:`v_1` und
:math:`v_2`, um die resultierende Geschwindigkeit zu erhalten.

*Beispiele:*

* Eine Person bewegt sich mit einer Geschwindigkeit :math:`v_1` auf einem
  Laufband entgegen der Laufbandgeschwindigkeit :math:`v_2`. Sind beide
  Geschwindigkeiten gleich groß, so bleibt die Person an der gleichen Stelle --
  die resultierende Geschwindigkeit :math:`v` ist gleich null.

  Sind beide Geschwindigkeiten unterschiedlich groß, so bewegt sich die Person
  in Richtung der größeren Geschwindigkeit. [#]_

* Stimmt die Bewegungsrichtung der Person mit der Richtung der
  Laufbandgeschwindigkeit überein, so addieren sich die Beträge beider
  Geschwindigkeiten. Die Geschwindigkeit :math:`v` der Person (relativ zum
  Erdboden) ist somit gleich :math:`v_1 + v_2`.

Die Addition der auftretenden Geschwindigkeiten ist auch möglich, wenn diese in
einem beliebigen Winkel zueinander stehen. Zeichnerisch stellt man dazu die
beiden Geschwindigkeiten :math:`\vec{v}_1` und :math:`\vec{v}_2`
als Pfeile dar, deren Richtungen mit denen der beiden Geschwindigkeiten
übereinstimmen und deren Längen die Beträge beider Geschwindigkeiten abbilden.
Nach den Regeln der :ref:`Vektor-Addition <gwm:Addition und Subtraktion von
Vektoren>` lässt sich damit aus beiden Geschwindigkeits-Pfeilen die Richtung und
der Betrag der resultierenden Geschwindigkeit :math:`\vec{v}` graphisch
ermitteln.

Betrag und Richtung der resultierenden Geschwindigkeit :math:`\vec{v}` können
auch rechnerisch bestimmt werden. Für eine zweidimensionale Bewegung (in einer
Ebene) gilt:

.. math::

    \vec{v} = \vec{v}_1 + \vec{v}_2 = \begin{pmatrix}
    v_{\mathrm{1x}} \\
    v_{\mathrm{1y}}
    \end{pmatrix}
    + \begin{pmatrix}
    v_{\mathrm{2x}} \\
    v_{\mathrm{2y}}
    \end{pmatrix} = \begin{pmatrix}
    v_{\mathrm{1x}} + v_{\mathrm{2x}} \\
    v_{\mathrm{1y}} + v_{\mathrm{2y}}
    \end{pmatrix}

Die resultierende Geschwindigkeit :math:`\vec{v}` entspricht somit einer
komponentenweisen Addition der beiden Geschwindigkeits-Vektoren
:math:`\vec{v}_{1}` und :math:`\vec{v}_{2}`. Für den Betrag der
resultierenden Geschwindigkeit :math:`v = | \, \vec{v} \, |` gilt:

.. math::

    v = \sqrt{v_1^2 + v_2^2}

Aus dem Verhältnis der :math:`y`- zur :math:`x`-Komponente lässt sich der
Winkel der resultierenden Geschwindigkeit bestimmen:

.. math::

    \tan{\varphi } = \frac{v_{\mathrm{y}}}{v_{\mathrm{x}}} \quad \Longleftrightarrow
    \quad \varphi = \tan ^{-1}{\left(\frac{v_{\mathrm{y}}}{v_{\mathrm{x}}}\right)}

*Beispiel:*

* Ein Boot überquert mit einer Geschwindigkeit :math:`v_1 =
  \unit[3]{\frac{m}{s}}` senkrecht einen Fluss, der mit einer Geschwindigkeit
  :math:`v_2 = \unit[1]{\frac{m}{s}}` strömt. Legt man ein Koordinatensystem so
  an, dass die :math:`y`-Achse in Richtung der Geschwindigkeit des Bootes und
  die :math:`x`-Achse in Richtung der Flussströmung zeigt, so folgt für die
  resultierende Geschwindigkeit :math:`\vec{v}`:

  .. math::

      \vec{v} = \vec{v}_1 + \vec{v}_2 = \begin{pmatrix}
      0 \\ 3
      \end{pmatrix} + \begin{pmatrix}
      1 \\ 0
      \end{pmatrix} = \begin{pmatrix}
      1 \\ 3
      \end{pmatrix}

  Der Betrag der resultierenden Geschwindigkeit ist hierbei:

  .. math::

      v = \sqrt{v_1^2 + v_2^2} = \sqrt{\left(\unit[1]{\frac{m}{s}}\right)^2 +
      \left( \unit[3]{\frac{m}{s}}\right)^2} = \sqrt{\unit[10]{\frac{m^2}{s^2}}}
      \approx \unit[3,16]{\frac{m}{s}}

  Der Winkel gegenüber der :math:`x`-Achse (Richtung des Flusses) beträgt:

  .. math::

      \alpha = \tan^{-1}{\left(\frac{v_{\mathrm{y}}}{v_{\mathrm{x}}}\right)} = \tan
      ^{-1}{\left( \frac{3}{1} \right)} \approx 71,6 \degree

  Das Boot driftet somit um einem Winkel von rund :math:`90\degree - 71,6\degree
  = 18,40\degree` ab.

Die in die jeweiligen Richtungen zurückgelegten Wegstrecken :math:`s_{\mathrm{x}}` und
:math:`s_{\mathrm{y}}` lassen sich komponentenweise über die Formel :math:`s = v \cdot t +
s_0` berechnen, wobei :math:`s_0` der anfänglichen Entfernung von der jeweiligen
Achse entspricht.


.. _Verallgemeinerung für dreidimensionale Geschwindigkeiten:

.. rubric:: Verallgemeinerung für dreidimensionale Geschwindigkeiten

Bei dreidimensionalen Bewegungen kann nach dem gleichen Rechenschema zusätzlich
eine :math:`z`-Komponente hinzu genommen werden. Für den Betrag jeder
(Teil-)Geschwindigkeit gilt dabei in allgemeiner Form:

.. math::

    v = |\vec{v}| = \sqrt{v_{\mathrm{x}}^2 + v_{\mathrm{y}}^2 + v_{\mathrm{z}}^2}{\color{white}\ldots}


Für die Summe der einzelnen Geschwindigkeiten gilt entsprechend:

.. math::

    \vec{v} = \vec{v}_1 + \vec{v}_2 = \begin{pmatrix}
    v_{\mathrm{1x}} \\
    v_{\mathrm{1y}} \\
    v_{\mathrm{1z}} \\
    \end{pmatrix}
    + \begin{pmatrix}
    v_{\mathrm{2x}} \\
    v_{\mathrm{2y}} \\
    v_{\mathrm{2z}} \\
    \end{pmatrix} = \begin{pmatrix}
    v_{\mathrm{1x}} + v_{\mathrm{2x}} \\
    v_{\mathrm{1y}} + v_{\mathrm{2y}} \\
    v_{\mathrm{1y}} + v_{\mathrm{2z}}
    \end{pmatrix}

Die Winkel :math:`\alpha ,\, \beta ,\, \gamma` zwischen der resultierenden
Geschwindigkeit und den drei Raumachsen :math:`x ,\, y ,\, z` lassen sich
berechnen, indem man die :ref:`Skalarprodukte <gwm:Skalarprodukt>`
:math:`\vec{v} \cdot \vec{e}_{\mathrm{x}}`, :math:`\vec{v} \cdot \vec{e}_{\mathrm{y}}` und
:math:`\vec{v} \cdot \vec{e}_{\mathrm{z}}` mit den Einheitsvektoren der jeweiligen
Richtungen bildet und diese nach den gesuchten Winkeln auflöst.

.. index:: Wurf

.. _Überlagerung zweier Bewegungen mit konstanter Beschleunigung:

Überlagerung zweier Bewegungen mit konstanter Beschleunigung
------------------------------------------------------------

Bei der Überlagerung zweier Bewegungen müssen die Geschwindigkeiten der beiden
Bewegungskomponenten nicht konstant sein. Nicht selten tritt der Fall auf, dass
eine (geradlinige) Bewegung mit konstanter Geschwindigkeit und eine Bewegung mit
konstanter Beschleunigung gleichzeitig stattfindet. Dies wird im Folgenden
anhand von Wurfvorgängen näher beschrieben.

.. index:: Wurf; senkrecht

.. _Senkrechter Wurf nach oben:

.. rubric:: Der senkrechte Wurf nach oben

Wird ein Gegenstand, beispielsweise ein Ball, senkrecht nach oben geworfen, so
bewegt er sich zunächst mit seiner ursprünglichen Geschwindigkeit :math:`v
_{\mathrm{0}}` entlang der :math:`z`-Achse nach oben. Durch die Erdbeschleunigung
:math:`g = \unit[9,81]{\frac{m}{s^2}}`, die entgegen der :math:`z`-Achse wirkt,
wird der Gegenstand in die umgekehrte Richtung konstant beschleunigt (der
Luftwiderstand soll vernachlässigt werden).

Zur Beschreibung der Bewegung wird das Koordinatensystem am besten so gewählt,
dass die :math:`z`-Achse senkrecht nach oben zeigt und sich ihr Nullpunkt an der
Abwurfstelle befindet. Da der Wurf senkrecht und somit entlang der
:math:`z`-Achse verläuft, kann der :math:`x`- und :math:`y`-Anteil der Bewegung
weggelassen werden, da er konstant gleich Null ist. Für den Vektor der
resultierenden Geschwindigkeit :math:`\vec{v}` gilt damit in Abhängigkeit von
der Zeit :math:`t`:

.. math::

    \vec{v} = v_{\mathrm{z}} = v_0 - g \cdot t

Für den zeitlichen Verlauf der zurückgelegten Wegstrecke gilt entsprechend:

.. math::

    {\color{white}.\;\;\,}\vec{s} = v_0 \cdot t - \frac{1}{2} \cdot g \cdot t^2

Mit den beiden obigen Gleichungen lässt sich die maximale Steighöhe :math:`s
_{\mathrm{max}}` sowie die Zeit :math:`t_{\mathrm{max}}`, welche der Gegenstand zum
Erreichen dieser Höhe benötigt, berechnen. Die Zeit :math:`t_{\mathrm{max}}` lässt
sich anhand der ersten Gleichung bestimmen; an diesem Punkt ist nämlich die
Geschwindigkeit des Gegenstands gleich Null. Somit gilt:

.. math::

    v_{\mathrm{0}} - g \cdot t_{\mathrm{max}} = 0 \quad \Leftrightarrow \quad
    t_{\mathrm{max}} = \frac{v_0}{g}

Setzt man die so bestimmte Zeit :math:`t_{\mathrm{max}}` in die zweite Gleichung
ein, so kann man entsprechend die maximale Steighöhe :math:`s_{\mathrm{max}}`
berechnen:

.. math::

    {\color{white}\ldots \qquad \quad \;}s_{\mathrm{max}} &= v_0 \cdot
    t_{\mathrm{max}} - \frac{1}{2} \cdot g \cdot t_{\mathrm{max}}^2 \\ 
    &= v_{\mathrm{0}} \cdot \frac{v_0}{g} - \frac{1}{2} \cdot g
    \cdot \left( \frac{v_0}{g}\right)^2 \\
    &= \frac{\phantom{..} v_0^2 \phantom{.}}{g} - \frac{1}{2} \cdot
    \frac{\phantom{..}v_0^2 \phantom{.}}{g} \\[6pt] 
    \Rightarrow s_{\mathrm{max}} &= \frac{v_0^2}{2 \cdot g}

Nach der doppelten Zeit, also :math:`2 \cdot t_{\mathrm{max}}`, kommt der
Gegenstand wieder auf dem Boden an. Dies lässt sich einerseits überprüfen, indem
man in die Weg-Zeit-Gleichung :math:`s = 0` setzt und die Gleichung nach
:math:`t` auflöst. Andererseits kann auch die Symmetrie der Parabel als
Begründung dienen: Die Wegstrecke wird beim Herunterfallen in der gleichen Weise
durchlaufen wie beim Hochwerfen, nur zeitlich umgekehrt. Entsprechend ist auch
die Geschwindigkeit des Gegenstands, sofern kein Luftwiderstand auftritt, vor
Aufprall wieder gleich der ursprünglichen Geschwindigkeit :math:`v_0`.


.. _Senkrechter Wurf nach unten:

.. rubric:: Der senkrechte Wurf nach unten

Kann ein geworfener Gegenstand -- beispielsweise im Anschluss an einen
senkrechten Wurf nach oben -- nach dem Erreichen seiner Ausgangslage weiter
herab fallen, so führt ab diesem diesem Zeitpunkt einen so genannten senkrechten
Wurf nach unten aus; seine Anfangsgeschwindigkeit beträgt dabei :math:`-v_0`.

Für die Geschwindigkeit :math:`\vec{v}` des Gegenstands gilt in Abhängigkeit von der
Zeit :math:`t`:

.. math::

    \vec{v} = v_{\mathrm{z}} = -v_0 - g \cdot t

Für den zeitlichen Verlauf der zurückgelegten Wegstrecke gilt entsprechend:

.. math::

    {\color{white}.}\vec{s} = -v_0 \cdot t -\frac{1}{2} \cdot g \cdot t^2

Das Koordinatensystem wurde ursprünglich so festgelegt, dass sich der Nullpunkt
der :math:`z`-Achse in Höhe der Abwurfstelle, also in einer Höhe :math:`z_0`
über dem Boden befindet. Der Gegenstand kann beim senkrechten Wurf nach unten
somit maximal die Wegstrecke :math:`s_{\mathrm{max}} = -z_0` zurücklegen. Die dafür
benötigte Zeit kann durch Umstellen der letzten Gleichung bestimmt werden:

.. math::

    -z_0 = -v_0 \cdot t - \frac{1}{2} \cdot g \cdot t^2 \quad \Leftrightarrow
    \quad \frac{1}{2} \cdot g \cdot t^2 + v_0 \cdot t - z_0 = 0

Diese quadratische Gleichung für :math:`t_{\mathrm{max}}` kann mit Hilfe der
:ref:`Mitternachtsformel <gwm:Quadratische Gleichungen>` gelöst werden. Ihre Lösung
lautet:

.. math::

    t_{\mathrm{max}} = \frac{-v_0 + \sqrt{v_0^2 + 2 \cdot g \cdot z_0}}{g}

Setzt man diese Zeit :math:`t` in die Geschwindigkeit-Zeit-Gleichung ein, so
folgt für die Geschwindigkeit :math:`v` des Gegenstands unmittelbar vor dem
Aufprall auf den Boden:

.. math::

    v_{\mathrm{max}} &= -v_0 - g \cdot \left(\frac{-v_0 + \sqrt{v_0^2 + 2 \cdot g
    \cdot z_0}}{g}\right) \\[5pt]
    &= -v_0 \;\;\; - \;\; \big( -v_0 + \sqrt{v_0^2 + 2 \cdot g \cdot z_0}\big)
    \\[8pt]
    &= - \sqrt{v_0^2 + 2 \cdot g \cdot z_0}

Gilt im Speziellen für die Anfangsgeschwindigkeit :math:`v_0 = 0`, so entspricht
das Ergebnis :math:`v = \sqrt{2 \cdot g \cdot z_0}` der Geschwindigkeit des
Gegenstands beim freien Fall.

..  Mit dieser Geschwindigkeit kann der Gegenstand beispielsweise nach einem elastischen
..  Aufprall auf dem Boden, wieder maximal die ursprüngliche Ausgangslage erreichen
..  (sofern der Luftwiderstand vernachlässigbar ist).

.. index:: Wurf; waagrecht

.. _Waagrechter Wurf:

.. rubric:: Der waagrechte Wurf

Wird ein Gegenstand, von einer erhöhten Position :math:`z_0` aus waagrecht geworfen,
so bewegt er sich -- unter Vernachlässigung des Luftwiderstands -- entlang der
horizontalen :math:`x`-Richtung mit seiner ursprünglichen Geschwindigkeit
:math:`v_{\mathrm{0}}` fort. In der vertikalen Richtung hingegen findet eine
gleichmäßig beschleunigte Bewegung entgegen der :math:`z`-Achse statt, bedingt
durch die Erdbeschleunigung :math:`g = \unit[9,81]{\frac{m}{s^2}}`.

Für den Vektor der resultierenden Geschwindigkeit :math:`\vec{v}` gilt damit in
Abhängigkeit von der Zeit :math:`t`: [#]_

.. math::

    \vec{v} = \begin{pmatrix} v_{\mathrm{x}} \\ v_{\mathrm{z}} \\ \end{pmatrix} =
    \begin{pmatrix} v_0 \\ - g \cdot t \end{pmatrix}{\color{white}\ldots}

Für den zeitlichen Verlauf der zurückgelegten Wegstrecke gilt entsprechend:

.. math::

    {\color{white}\ldots \quad \; }\vec{s} = \begin{pmatrix} s_{\mathrm{x}} \\
    s_{\mathrm{z}} \\
    \end{pmatrix} =
    \begin{pmatrix} v_0 \cdot t \\[3pt] - \frac{1}{2} \cdot g \cdot t^2 + z_0
    \end{pmatrix}

Die maximale Flugzeit :math:`t_{\mathrm{max}}` lässt sich aus der
:math:`z`-Komponente des zurückgelegten Weges bestimmen. Gilt nämlich
:math:`s_{\mathrm{z}} = 0`, so ist der Gegenstand auf dem Boden aufgekommen. Für
die zugehörige Zeit :math:`t_{\mathrm{max}}` gilt somit:

.. math::

    - \frac{1}{2} \cdot g \cdot t_{\mathrm{max}} + z_0 = 0 \quad
      \Leftrightarrow \quad t_{\mathrm{max}} = \sqrt{\frac{2 \cdot z_0}{g}}

Damit lässt sich ebenso die maximale Wurfweite :math:`s_{\mathrm{x,max}}` bestimmen:

.. math::

   s  _{\mathrm{x,max}} = v_{\mathrm{0}} \cdot t_{\mathrm{max}} = v_0  \cdot \sqrt{\frac{2
   \cdot z_{\mathrm{0}}}{g}}

.. index:: Wurf; schief

.. _Schiefer Wurf:

.. rubric:: Der schiefe Wurf

Wird ein Gegenstand gegenüber der Horizontalen in einem Winkel :math:`\alpha`
abgeworfen :math:`(0 < \alpha < 90\degree)`, so spricht man von einem schiefen
Wurf. Die Bewegung hat dabei, sofern der Luftwiderstand vernachlässigt werden
kann, stets einen parabelförmigen Verlauf. Um dies zu erklären, kann man sich
die Bewegung als zwei unabhängig voneinander stattfindende Teilbewegungen
vorstellen: Eine geradlinige Bewegung mit einer konstanter Geschwindigkeit
:math:`v_{\mathrm{x}}` in horizontaler Richtung und eine geradlinige Bewegung mit der
konstanten Beschleunigung :math:`g` in vertikaler Richtung.

Für die Komponenten :math:`v_{\mathrm{\mathrm{0x}}}` und :math:`v_{\mathrm{0z}}`
der Geschwindigkeit :math:`v_0` des Gegenstands beim Abwurf gilt:

.. math::
    :label: eqn-schiefer-wurf-start

    \vec{v}_0 = \begin{pmatrix}
    v_{\mathrm{\mathrm{0x}}} \\
    v_{\mathrm{0z}} \\
    \end{pmatrix} = \begin{pmatrix}
    v_0 \cdot \cos{(\alpha)}\\
    v_0 \cdot \sin{(\alpha})\\
    \end{pmatrix}

Ohne Luftwiderstand bleibt die horizontale Komponente der Geschwindigkeit
unverändert. In vertikaler Richtung wird der Gegenstand hingegen -- wie beim
senkrechten Wurf nach oben -- mit der Beschleunigung :math:`\unit[9,81]{m/s^2}`
zum Erdmittelpunkt hin beschleunigt. Für die Geschwindigkeit :math:`\vec{v}`
gilt somit in Abhängigkeit von der Zeit :math:`t`:

.. math::
    :label: eqn-schiefer-wurf-geschwindigkeit

    \vec{v} = \begin{pmatrix}
    v_{\mathrm{x}}\\
    v_{\mathrm{z}} \\
    \end{pmatrix}
    = \begin{pmatrix}
    v_{\mathrm{\mathrm{0x}}} \\
    v_{\mathrm{0z}} - g \cdot t
    \end{pmatrix}

Es findet also eine Überlagerung einer Bewegung mit konstanter Geschwindigkeit
in :math:`x`-Richtung und einer Bewegung mit konstanter Beschleunigung in
:math:`z`-Richtung statt. Für die in beiden Richtungen zurückgelegten
Wegstrecken :math:`s_{\mathrm{x}}` und :math:`s_{\mathrm{y}}` gilt:

.. math::
    :label: eqn-schiefer-wurf-wegstrecke

    \vec{s} = \begin{pmatrix}
    s_{\mathrm{x}}\\
    s_{\mathrm{z}} \\
    \end{pmatrix}
    = \begin{pmatrix}
    v_{\mathrm{0x}} \cdot t \\
    v_{\mathrm{0z}} \cdot t - \frac{1}{2} \cdot g \cdot t^2
    \end{pmatrix}

Hierbei wurde angenommen, dass der Gegenstand aus einer Höhe :math:`s_{\mathrm{0z}} =
\unit[0]{m}` geworfen wurde. Ist :math:`s_{\mathrm{0z}} \ne 0`, so muss diese Höhe zur
:math:`z`-Komponente addiert werden.

Wie beim senkrechten Wurf gilt für die Zeit :math:`t`, in welcher der Körper die
maximale Steighöhe :math:`s_{\mathrm{z,max}}` erreicht:

.. math::

    v_{\mathrm{0z}} - g \cdot t_{\mathrm{z,max}} = 0 \quad \Leftrightarrow \quad
    t_{\mathrm{z,max}} = \frac{v_{\mathrm{0z}}}{g}

Setzt man diese Zeit in die Bewegungsgleichung für die :math:`z`-Komponente
ein, so folgt für die maximale Steighöhe :math:`s_{\mathrm{z,max}}`:

.. math::
    :label: eqn-schiefer-wurf-wurfhoehe

    s_{z,\mathrm{max}} = v_{\mathrm{0z}} \cdot \frac{v_{\mathrm{0z}}}{g} - \frac{1}{2}
    \cdot g \cdot \left( \frac{v_{\mathrm{0z}}}{g} \right)^2 = \frac{v_{\mathrm{0z}}^2}{g} -
    \frac{1}{2} \cdot g \cdot \frac{v_{\mathrm{0z}}^2}{g^2} = \frac{v_{\mathrm{0z}}^2}{2 \cdot g}

..  Wird der Gegenstand aus einer Höhe :math:`h=0` abgeworfen, so ist die Wurfweite
..  am höchsten, wenn :math:`\alpha = 45\degree` ist. Die Wurfweite :math:`s_{\mathrm{x}}`
..  beträgt in diesem Fall

Die Wurfweite kann man für den obigen Fall :math:`(s_{\mathrm{0z}} = 0)` einfach
berechnen, indem man bedenkt, dass die Wurfbahn parabelförmig und damit
symmetrisch ist; die Zeit bis zum Aufprall auf dem Boden muss somit doppelt so
lang sein wie die Zeit :math:`t_{\mathrm{z,max}}` zum Erreichen der maximalen
Steighöhe. In dieser Zeit bewegt sich der Gegenstand in horizontaler Richtung um
folgende Wegstrecke:

.. math::
    :label: eqn-schiefer-wurf-wurfweite

    s_{\mathrm{x,max}} = v_{\mathrm{0x}} \cdot (2 \cdot t_{\mathrm{z,max}}) = v_0 \cdot
    \cos{\alpha} \cdot 2 \cdot \frac{v_0 \cdot \sin{\alpha}}{g} = \frac{v_0^2
    \cdot 2 \cdot \sin{\alpha} \cdot \cos{\alpha}}{g} = \frac{v_{\mathrm{0}}^2
    \cdot \sin{(2 \cdot \alpha)}}{g}

Hierbei wurde im letzten Rechenschritt das Additionstheorem für Sinus-Funktionen
genutzt. [#]_ Die Wurfweite ist also -- ebenfalls wie die Wurfhöhe -- vom
Wurfwinkel :math:`\alpha` abhängig. Für :math:`\alpha = 45\degree` ist im
obigen Fall :math:`\sin{(2 \cdot \alpha)} = \sin{(90 \degree)} = 1` und somit die
Wurfweite maximal :math:`(s_{\mathrm{x \, max,45\degree}} = \frac{v_0^2}{g})`.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Definiert man die Bewegungsrichtung der Person (nach rechts) als positiv,
     so kann der Betrag der resultierenden Geschwindigkeit als Differenz beider
     Geschwindigkeiten :math:`v_1 - v_2` berechnet werden. Gilt :math:`v_2 >
     v_1`, so ist die resultierende Geschwindigkeit "negativ", sie verläuft
     somit von rechts nach links.

     Schreibt man die Differenz :math:`v_1 - v_2` als Summe :math:`v_1 +
     (-v_2)`, so zeigt sich, dass auch in diesem Fall -- unter Berücksichtigung
     der Bewegungsrichtungen -- die resultierende Geschwindigkeit gleich der
     Summe der Einzelgeschwindigkeiten ist.

.. [#] Die :math:`y`-Komponente der Bewegung ist in diesem Fall konstant gleich
    Null und kann kann daher weggelassen werden, sofern die  :math:`x`-Achse in
    Wurfrichtung zeigt. In der Tat handelt es sich bei einem Wurf um eine
    zweidimensionale Bewegung innerhalb der :math:`xz`-Ebene.

.. [#] Das Additionstheorem für Sinus-Funktionen lautet allgemein:

    .. math::

        \sin{(\alpha_1 + \alpha_2)} = \sin{(\alpha_1)} \cdot \cos{(\alpha_2)} +
        \cos{(\alpha_1)} \cdot \sin{(\alpha_2)}

    Mit :math:`\alpha = \alpha_1 = \alpha_2` folgt somit :math:`\sin{(2 \cdot
    \alpha)} = 2 \cdot \sin{(\alpha)} \cdot \cos{(\alpha)}`.


.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Zusammengesetzte
    Bewegungen>`.

.. :ref:`Experimente <Experimente zu zusammengesetzten Bewegungen>` und 
