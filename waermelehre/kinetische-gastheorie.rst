
.. index:: Kinetische Gastheorie
.. _Kinetische Gastheorie:

Die kinetische Gastheorie
=========================

Viele reale Gase können unter Standardbedingungen in guter Näherung mittels
des Modells der idealen Gase beschrieben werden: Die Anziehungskräfte zwischen
den einzelnen Teilchen ist meist vernachlässigbar gering, und ebenso ist das
Volumen der einzelnen Teilchen klein im Vergleich zum Gesamtvolumen des Gases.
Geht man von diesen Annahmen aus, so kann ein Gas als große Anzahl einzelner
Atome oder Moleküle angesehen werden, die sich mit unterschiedlichen
Geschwindigkeiten in unterschiedliche Richtungen bewegen, wobei die einzelnen
Bewegungsrichtungen und Geschwindigkeiten statistisch verteilt sind.

In einem einfachen Modell kann man von einem einzelnen Gasteilchen ausgehen, das
sich in einem kubischen Behälter in :math:`x`-Richtung auf die linke Wand des
Behälters zu bewegt. Bezeichnet man mit :math:`m` die Masse des Gasteilchens und
mit :math:`-v _x` seine ursprüngliche Geschwindigkeit, so gilt für die
:ref:`Impulsänderung <Impuls>`, die das Teilchen bei einem elastischen Stoß mit
der Wand erfährt:

.. math::

    \Delta (m \cdot v) = m \cdot v_x - (- m \cdot v_x) = 2 \cdot m \cdot v_x

Bis das Teilchen wieder auf die linke Wand trifft, muss es eine Strecke von
:math:`s_x = 2 \cdot l` zurücklegen, wenn :math:`l` die Länge des Würfels ist.
Bis zum nächsten Stoß mit der linken Wand vergeht somit folgende Zeit
:math:`\Delta t`:

.. math::

    \Delta t = \frac{s_x}{v_x} = \frac{2 \cdot l}{v_x}

Die Kraft, die das Teilchen auf die Wand ausübt, ist gleich der Impulsänderung
je Zeit:

.. math::

    F = \frac{\Delta (m \cdot v)}{\Delta t} = \frac{2 \cdot m \cdot v_x}{\frac{2
    \cdot l}{v_x}} = \frac{m \cdot v_x^2}{l}

Der Druck, der von dem einzelnen Teilchen auf die linke Wand ausgeübt wird, ist
gleich dem Quotienten aus Kraft und Wandfläche:

.. math::

    p = \frac{F}{A} = \frac{m \cdot v_x^2}{A \cdot l}
    = \frac{2 \cdot m \cdot v_x^2}{V}

Im letzten Rechenschritt wurde die Beziehung :math:`V = A \cdot l` verwendet.
Geht man nun nicht von einem einzelnen, sondern von :math:`N` Teilchen aus, die
sich in :math:`x`-Richtung mit den Geschwindigkeiten :math:`v _{x,1}, \, v
_{x,2},\, \ldots,\, v _{x,n}`  hin- und herbewegen, so addieren sich die
einzelnen Beiträge zum Gesamtdruck:

.. math::

    p = \frac{F}{A} = \frac{m}{V} \cdot ( v _{x,1}^2 + v _{x,2}^2 +
    \ldots + v _{x,n}^2)

Da in einem Gasvolumen üblicherweise sehr viele Teilchen vorkommen, ist es
wesentlich praktischer, anstelle von :math:`N` einzelnen
Geschwindigkeits-Quadraten mit :math:`N`-mal dem mittleren
Geschwindigkeits-Quadrat der Teilchen zu rechnen. Dieses entspricht dem
arithmetischen Mittel der einzelnen Werte:

.. math::

    \bar{v_x}^2 = \frac{v _{x,1}^2 + v _{x,2}^2 +
    \ldots + v _{x,n}^2}{N} \quad \Longleftrightarrow \quad v _{x,1}^2 + v _{x,2}^2 +
    \ldots + v _{x,n}^2 = N \cdot \bar{v_x}^2

Setzt man diesen Ausdruck in die obige Gleichung ein, so erhält man:

.. math::

    p = \frac{m}{V} \cdot N \cdot \bar{v_x}^2

Bei der Bewegung der Gasteilchen im Behälter tritt keine
Geschwindigkeitsrichtung bevorzugt auf. Wenn sich im Durchschnitt gleich
viele Gasteilchen in :math:`x`-, :math:`y`- und :math:`z`-Richtung bewegen, muss
:math:`\bar{v_x}^2 = \bar{v_y}^2 = \bar{v_z}^2` gelten.

.. math::

    \bar{v}^2 = \bar{v_x}^2 + \bar{v_y}^2 + \bar{v_z}^2 \quad
    \Longleftrightarrow \quad \bar{v_x}^2 = \frac{1}{3} \cdot \bar{v}^2

Somit kann die obige Gleichung in folgender Form geschrieben werden:

.. math::

    p &= \frac{1}{3} \cdot \frac{N}{V} \cdot m \cdot \bar{v}^2 \\ &= \frac{1}{3}
    \cdot \frac{N}{V} \cdot 2 \cdot \frac{1}{2} \cdot m \cdot \bar{v}^2

Im letzten Rechenschritt wurde der Term auf der rechten Seite mit :math:`1 = 2
\cdot \frac{1}{2}` multipliziert, was den Wert des Terms zwar unverändert
lässt, es allerdings ermöglicht, den Faktor :math:`\left( \frac{1}{2} \cdot m
\cdot \bar{v}^2\right)` als mittlere kinetische Energie
:math:`\bar{E}_{\rm{kin}}` der Gasteilchen aufzufassen. Formt man die Gleichung
weiter um, so folgt:

.. math::

    p \cdot V = \frac{2}{3} \cdot N \cdot \bar{E}_{\rm{kin}}

Der Ausdruck :math:`p \cdot V` auf der linken Gleichungsseite entspricht nach
der :ref:`allgemeinen Gasgleichung <Allgemeine Gasgleichung>` gerade :math:`p
\cdot V = n \cdot R \cdot T`. Anstelle der allgemeinen Gaskonstante :math:`R`
kann dabei auch :math:`R = N _{\rm{A}} \cdot k _{\rm{B}}` gesetzt werden, wobei :math:`k
_{\rm{B}} = \unit[1,38 \cdot 10 ^{-23}]{\frac{J}{K}}` die so genannte `Boltzmann
<https://de.wikipedia.org/wiki/Ludwig_Boltzmann>`_-Konstante ist. [#]_ Für
:math:`n=\unit[1]{mol}` eines Gases gilt also:

.. math::

    N \cdot k _{\rm{B}} \cdot T = \frac{2}{3} \cdot N \cdot \bar{E}_{\rm{kin}}

Damit erhält man als Gesamtergebnis der kinetischen Gastheorie folgende
Gleichung:

.. math::
    :label: eqn-kinetische-gastheorie

    \bar{E}_{\rm{kin}} = \frac{3}{2} \cdot k _{\rm{B}} \cdot T

Die kinetische Energie der Gasteilchen nimmt somit direkt proportional mit der
(absoluten) Temperatur des Gases zu. Mit Hilfe der Gleichung
:eq:`eqn-kinetische-gastheorie` kann einerseits bestimmt werden, welche
kinetische Gesamtenergie die Teilchen einer Gasmenge bei einer bestimmten
Temperatur aufweisen, andererseits allerdings auch berechnet werden, wie groß
die durchschnittliche Geschwindigkeit der einzelnen Gasteilchen bei einer
bestimmten Temperatur ist.

*Beispiele:*

* Wie groß ist die kinetische Gesamtenergie aller Moleküle eines idealen Gases
  bei einer Temperatur von :math:`\unit[0]{\degree C}` und einer Stoffmenge von
  :math:`n= \unit[1]{mol}`?

  Nach der kinetischen Gastheorie gilt für die durchschnittliche kinetische
  Energie eines einzelnen Gasteilchens:

  .. math::

     \bar{E}_{\rm{kin}} = \frac{3}{2} \cdot k _{\rm{B}} \cdot T = \frac{3}{2}
     \cdot \unit[1,38 \cdot 10 ^{-23}]{\frac{J}{K}} \cdot \unit[273]{K} \approx
     \unit[5,65 \cdot \unit[10]{-21}]{J}

  Multipliziert man diesen Wert mit der Anzahl :math:`N _{\rm{A}} = \unit[6,022
  \cdot 10 ^{23}]{\frac{1}{mol}}` an Teilchen je Mol, so erhält man als
  Gesamtenergie für ein Mol an Teilchen:

  .. math::

      \bar{E}_{\rm{kin,ges}} = \unit[5,65 \cdot 10 ^{-21}]{J} \cdot \unit[6,022
      \cdot 10 ^{23}]{\frac{1}{mol}} \approx \unit[3403]{\frac{J}{mol}}

  Unter :ref:`Normalbedingungen <Normalvolumen>` hat ein Mol eines idealen Gases
  ein Volumen von rund :math:`\unit[22,4]{l}`. Die darin enthaltene kinetische
  Energie :math:`E _{\rm{kin,ges}} \approx  \unit[3,4]{kJ}` aller Teilchen
  entspricht in etwa der kinetischen Energie eines :math:`m=\unit[1]{kg}`
  schweren Gegenstands, der sich mit einer Geschwindigkeit von
  :math:`v=\unit[82,5]{\frac{m}{s}} \approx \unit[297]{\frac{km}{h}}` bewegt.
  Diese beachtliche Energiemenge ist beispielsweise der Grund dafür, weshalb
  Wärmepumpen einen Teil der kinetischen Teilchen-Energien einer kälteren
  Umgebung "abzapfen" und einer wärmeren Umgebung zuführen können.

* Wie groß ist die Wurzel aus dem mittleren Geschwindigkeitsquadrat
  :math:`\bar{v}^2` von Luftmolekülen bei :math:`T = \unit[20]{\degree C}`?

  Nach der kinetischen Gastheorie gilt für die durchschnittliche kinetische
  Energie eines einzelnen Gasteilchens der Masse :math:`m`:

  .. math::

      \bar{E}_{\rm{kin}} = \frac{1}{2} \cdot m \cdot \bar{v}^2 = \frac{3}{2}
      \cdot k _{\rm{B}} \cdot T \quad \Longleftrightarrow \quad \bar{v}^2 =
      \frac{3 \cdot k _{\rm{B}} \cdot T}{m}

  Wie im Abschnitt :ref:`Teilchenzahl und molare Masse <Teilchenzahl und molare
  Masse>` gezeigt, beträgt die Masse von einem Mol an Stickstoff-Teilchen
  :math:`\unit[28]{g}`, die Masse von einem Mol an Sauerstoff-Teilchen
  :math:`\unit[32]{g}`. Teilt man diese Werte jeweils durch die Anzahl :math:`N
  _{\rm{A}} = \unit[6,022 \cdot 10 ^{23}]{\frac{1}{mol}}` an Teilchen je Mol,
  so erhält man als Masse eines Stickstoff- bzw. Sauerstoff-Teilchens:

  .. math::

      m _{\ce{N2}} = \frac{\unit[28]{\frac{g}{mol}}}{\unit[6,022 \cdot 10
      ^{-23}]{\frac{1}{mol}}} \approx \unit[4,65 \cdot 10 ^{-23}]{g} =
      \unit[4,65 \cdot 10 ^{-26}]{kg}  \\
      m _{\ce{O2}} = \frac{\unit[32]{\frac{g}{mol}}}{\unit[6,022 \cdot 10
      ^{-23}]{\frac{1}{mol}}} \approx \unit[5,31 \cdot 10 ^{-23}]{g} =
      \unit[5,31 \cdot 10 ^{-26}]{kg}

  Setzt man diese Werte in die obige Gleichung ein, so erhält man für die
  Geschwindigkeiten der Stickstoff- und Sauerstoffmoleküle:

  .. math::

      \sqrt{\bar{v}_{\ce{N2}}^2} = \sqrt{\frac{3 \cdot \unit[1,38 \cdot 10
      ^{-23}]{\frac{J}{K}} \cdot \unit[(273+20)]{K}}{\unit[4,6 \cdot 10
      ^{-26}]{kg}}} \approx \unit[511]{\frac{m}{s}} \\
      \sqrt{\bar{v}_{\ce{O2}}^2} = \sqrt{\frac{3 \cdot \unit[1,38 \cdot 10
      ^{-23}]{\frac{J}{K}} \cdot \unit[(273+20)]{K}}{\unit[5,3 \cdot 10
      ^{-26}]{kg}}} \approx \unit[478]{\frac{m}{s}} \\


  Die Stickstoffteilchen sind mit rund :math:`\unit[480]{\frac{m}{s}} \approx
  \unit[1840]{\frac{km}{h}}` somit schneller als die Sauerstoffteilchen mit
  :math:`\unit[511]{\frac{m}{s}} \approx \unit[1720]{\frac{km}{h}}`.

Je geringer also die molare Masse eines Gases ist, desto höher ist bei einer
bestimmten Temperatur die durchschnittliche Geschwindigkeit der enthaltenen
Teilchen.

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Mit :math:`N _{\rm{A}} = \unit[6,022 \cdot 10 ^{23}]{\frac{1}{mol}}` ist
    die sogenannte Avogadro-Konstante gemeint, welche die Anzahl an Teilchen je
    mol eines chemischen Stoffes angibt.


