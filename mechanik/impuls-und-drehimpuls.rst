.. meta:: 
    :keywords:  Impuls, Impulserhaltung, Drehimpuls, Drehimpulserhaltung

.. _Impuls und Drehimpuls:

Impuls und Drehimpuls
=====================

Neben der Energie gibt es zwei weitere Größen, die innerhalb eines
abgeschlossenen Systems stets konstant bleiben; sie werden als Impuls und
Drehimpuls bezeichnet. Die Impulsgesetze werden insbesondere bei mathematischen
Beschreibung von Stoßprozessen genutzt, Drehimpulse sind bei Kreisbewegungen und
Rotationen von Bedeutung.

.. index:: Impuls
.. _Impuls:

Der Impuls
----------

Der Bewegungszustand eines Körpers ist neben seiner Geschwindigkeit auch durch
seine Masse gekennzeichnet. Der Impuls eines Körpers kennzeichnet die Wucht, die
dieser Körper bei einer Translationsbewegung (:ref:`geradlinige <Geradlinige
Bewegung>`, :ref:`kreisförmige <Kreisförmige Bewegung>` oder
:ref:`zusammengesetzte <Zusammengesetzte Bewegungen>` Bewegung) hat.

*Definition:*

    Der Impuls :math:`\vec{p}` eines Körpers ist gleich dem Produkt aus seiner
    Masse :math:`m` und seiner Geschwindigkeit :math:`\vec{v}`:

    .. math::
        :label: eqn-impuls
        
        \vec{p} = m \cdot \vec{v} 

*Einheit:*

    Die Einheit des Impulses ist gemäß der Definition :math:`\unit[1]{kg \cdot
    \frac{m}{s}}`.

Der Impuls :math:`\vec{p}` ist eine vektorielle Größe und zeigt in die gleiche
Richtung wie die Geschwindigkeit :math:`\vec{v}`. Der Impuls eines Körpers
ändert sich, wenn sich entweder seine Geschwindigkeit ändert (in Betrag oder
Richtung), oder wenn sich -- beispielsweise bei einem Raketenstart -- seine
Masse ändert. 

Mathematisch lässt sich die betragliche Änderung des Impulses somit
folgendermaßen ausdrücken:

.. math::
    
    \Delta p = m \cdot \Delta v + \Delta m \cdot v{\color{white}\quad \;\;\; \ldots}

Diese Änderung des Impulses kann in Relation zur Zeit :math:`\Delta t` gesetzt
werden, in der die Änderung stattfindet. Damit folgt:

.. math::
    
    {\color{white}\ldots \qquad \qquad \quad   }\frac{\Delta p}{\Delta t} &=
    \frac{m \cdot \Delta v + \Delta m \cdot v}{\Delta t} = \frac{m \cdot \Delta
    v}{\Delta t} + \frac{\Delta m \cdot v}{\Delta t} \\[4pt]
    &= m \cdot \frac{\Delta v}{\Delta t} + \frac{\Delta m}{\Delta t} \cdot v

Der Term :math:`m \cdot \frac{\Delta v}{\Delta t}` im ersten Teil dieser Summe
kann aufgrund des Zusammenhangs :math:`a = \frac{\Delta v}{\Delta t}` auch als
:math:`m \cdot a` geschrieben werden. Dieser Term entspricht der üblichen
Definition der Kraft :math:`(F = m \cdot a)` und ist mit der Änderung des
Impulses identisch, sofern die Änderung der Masse gleich Null ist.
Andernfalls muss das :ref:`2. Newtonsche Gesetz ("Kraftgesetz") <Kraftgesetz>`
allgemeiner formuliert werden. Newton selbst hat es in folgender Form angegeben:

.. math::
    :label: eqn-kraftgesetz-allgemein
    
    {\color{white}\ldots}\vec{F} = \frac{\Delta \vec{p}}{\Delta t} = m \cdot
    \vec{a} + \frac{\Delta
    m}{\Delta t} \cdot \vec{v}

.. index:: Kraftstoß

Eine Kraft kann somit als zeitliche Änderung des Impulses aufgefasst werden.
Umgekehrt kann man sich eine Impulsänderung :math:`\Delta \vec{p}` als
"Kraftstoß" vorstellen, der sich ergibt, wenn eine Kraft :math:`\vec{F}` über
einen Zeitraum :math:`\Delta t` auf einen Körper einwirkt. Es gilt also:

.. math::
    
    \Delta \vec{p} = \vec{F} \cdot \Delta t

.. Kraft nicht konstant -> Integral von F(t) über dt

.. index:: Impulserhaltungssatz, Stoßprozesse
.. _Impulserhaltungssatz:

.. rubric:: Der Impulserhaltungssatz

Ein System aus mehreren miteinander wechselwirkenden Körpern hat einen
Gesamtimpuls, der der Summe aller Einzelimpulse entspricht: 

.. math::
    :label: eqn-gesamtimpuls
    
    \vec{p} _{\rm{ges}} = \sum_{i=1}^{n} m_{\rm{i}} \cdot \vec{v} _{\rm{i}} = m_1
    \cdot \vec{v}_1 + m_2 \cdot \vec{v}_2 + \ldots + m _{\rm{n}} \cdot
    \vec{v}_{\rm{n}}

Wenn keine äußeren Kräfte auf das System wirken, dann ist der Gesamtimpuls
konstant. Dieser empirisch gefundene Sachverhalt wird Impulserhaltung genannt
und stellt neben der :ref:`Erhaltung der Energie <Energieerhaltungssatz>` einen
der wichtigsten Erhaltungssätze in der Physik dar.


.. index:: 
    single: Stoßprozesse; elastisch
.. _Elastischer Stoß zweier Kugeln:

.. rubric:: Beispiel 1\: Elastischer Stoß zweier Kugeln

Besteht ein System beispielsweise aus zwei Kugeln, die frontal und elastisch
zusammenstoßen, so ist sowohl die Summe der Impulse wie auch die Summe der
Bewegungsenergien vor und nach der Wechselwirkung gleich. Bezeichnet man mit
:math:`v` eine Geschwindigkeit *vor* und mit :math:`u` eine Geschwindigkeit
*nach* dem Stoß, so ergibt sich nach dem Impuls- und Energieerhaltungssatz
folgendes Gleichungssystem:

.. math::
    
    m_1 \cdot v_1 + m_2 \cdot v_2 &= m_1 \cdot u_1 +  m_2 \cdot u_2
    \\[4pt] \frac{1}{2} \cdot m_1 \cdot v_1^2 \, + \, \frac{1}{2}\cdot m_2 \cdot v_2^2 &=
    \frac{1}{2} \cdot m_1 \cdot u_1^2 \, + \, \frac{1}{2} \cdot m_2 \cdot u_2^2

Da in der zweiten Gleichung alle Terme den Faktor :math:`\frac{1}{2}` enthalten,
kann dieser ausgeklammert und gekürzt werden. Durch Umstellen der Terme können
beide Gleichungen auf folgende Form gebracht werden:

.. math::
    
    m_1 \cdot (v_1 - u_1) &= m_2 \cdot (v_2 - u_2) \\[4pt]
    m_1 \cdot (v_1^2 - u_1^2) &= m_2 \cdot (v_2^2 - u_2^2)

Da :math:`m_1` und :math:`m_2` ungleich Null sind und -- als Bedingung für einen
Stoß -- zusätzlich :math:`v \ne u` ist, kann zur Lösung des Gleichungssystems
die zweite Gleichung (nach Anwendung der binomischen Formel) durch die erste
geteilt werden. [#]_ Das Ergebnis lautet:

.. math::
    
    v_1 + u_1 = v_2 + u_2 

Diese Gleichung wurde durch Anwendung äquivalenter Umformungen aus der
ursprünglichen Energieerhaltungs-Gleichung gebildet. Gemeinsam mit der
ursprünglichen Impulserhaltungs-Gleichung stellt sie ein nun ein *lineares*
Gleichungssystem dar:

.. math::
    
    m_1 \cdot v_1 + m_2 \cdot v_2 &= m_1 \cdot u_1 +  m_2 \cdot u_2 \\
    v_1 - v_2 &= -u_1 + u_2 

Die beiden gesuchten Größen :math:`u_1` und :math:`u_2` stehen dabei jeweils
auf der rechten Seite. Löst man die beispielsweise die zweite Gleichung nach
:math:`u_2` auf und setzt das Ergebnis :math:`u_2 = u_1 + v_1 - v_2` in die
erste Gleichung ein, so erhält man:

.. math::
    
   {\color{white}\ldots \qquad \qquad } m_1 \cdot v_1 + m_2 \cdot v_2 &= m_1 \cdot u_1 + m_2 \cdot (u_1 + v_1 - v_2)

Dies ergibt, wenn man die rechte Seite ausmultipliziert und die Gleichung nach
:math:`u_1` auflöst:

.. math::
    :label: eqn-elastischer-stoss-u1
    
    u_1 = \frac{2 \cdot m_2 \cdot v_2 + (m_1 - m_2) \cdot v_1}{m_1 + m_2}

Entsprechend ergibt sich für die Geschwindigkeit :math:`u_2`:

.. math::
    :label: eqn-elastischer-stoss-u2
    
    u_2 = \frac{2 \cdot m_1 \cdot v_1 + (m_2 - m_1) \cdot v_2}{m_1 + m_2}

Diese beiden Ergebnisse gelten für beliebige Kugelmassen und
Anfangsgeschwindigkeiten. Betrachtet man einige Sonderfälle, so erhält man
folgende vereinfachte Ergebnisse:

* Sind beide Kugeln gleich schwer (:math:`m_1 = m_2`) und ist die zweite anfangs
  in Ruhe :math:`(v_2 = 0)`, so überträgt die erste Kugel beim Stoß ihren
  gesamten Impuls auf die zweite Kugel. Es gilt nämlich in diesem Fall: 

  .. math::
      
      u_1 &= \frac{2 \cdot m_1 \cdot 0 \; + 0 \cdot v_1}{2 \cdot m_1} = 0 \\[4pt]
      u_2 &= \frac{2 \cdot m_1 \cdot v_1 + 0 \cdot v_2}{2 \cdot m_1} = v_1
  
* Ist die erste Kugel sehr viel leichter als die zweite Kugel und ruht diese
  (:math:`m_1 \ll  m_2` und :math:`v_2 = 0`), so prallt die erste Kugel mit einer
  (nahezu) gleich großen, jedoch entgegengesetzt gerichteten Geschwindigkeit
  zurück. Es gilt in diesem Fall näherungsweise:

.. math::
    
      {\color{white}\ldots \qquad \quad }u_1 &\approx  \frac{2 \cdot m_2 \cdot 0
      - m_2 \cdot v_1}{m_2} = -v_1 \\[4pt]
      u_2 &\approx \phantom{\ldots}\;\; \frac{ \phantom{\ldots}0 \cdot v_2
      \phantom{\ldots}}{m_2} \phantom{\ldots}\;\, = 0
  
* Ist die erste Kugel sehr viel schwerer als die zweite Kugel und ruht diese
  (:math:`m_1 \gg  m_2` und :math:`v_2 = 0`), so bewegt sich die erste Kugel mit
  nahezu gleicher Geschwindigkeit weiter; die zweite Kugel wird auf die doppelte
  Geschwindigkeit der ersten Kugel beschleunigt. Es gilt in diesem Fall
  näherungsweise:

.. math::
    
      {\color{white}\ldots \qquad \quad }u_1 &\approx  \frac{2 \cdot m_2 \cdot 0
      + m_1 \cdot v_1}{m_1} = +v_1 \\[4pt]
      u_2 &\approx \frac{ 2 \cdot m_1 \cdot v_1 - m_1 \cdot 0}{m_1} \approx 2
      \cdot v_1

Stoßen die Kugeln nicht frontal, sondern schräg aufeinander, so muss das obige
Rechenschema komponentenweise für die drei Raumrichtungen komponentenweise
angewendet werden.

.. index:: 
    single: Stoßprozesse; unelastisch

.. _Unelastischer Stoß zweier Kugeln:

.. rubric:: Beispiel 2\: Unelastischer Stoß zweier Kugeln

Stoßen zwei Kugeln unelastisch aufeinander, so bewegen sich beide nach dem Stoß
mit der gleichen Geschwindigkeit :math:`u` entlang einer gemeinsamen Richtung
hin fort. Die Richtung und der Betrag der Geschwindigkeit :math:`u` kann anhand
des Impulserhaltungs-Gleichung direkt berechnet werden:

..  "Impulssatz"?

.. math::
    
    u = \frac{m_1 \cdot v_1 + m_2 \cdot v_2}{m_1 + m_2}

Der Energie-Erhaltungssatz gilt hingegen in diesem Fall nicht -- durch die
unelastische Verformung wird mechanische Energie in Wärme umgewandelt. [#]_ 

.. _Teilelastischer Stoß:

.. rubric:: Teilelastische Stoßprozesse

In vielen Fällen handelt es sich bei Stößen weder einem komplett elastischen
noch um einen komplett unelastischen Vorgang, sondern vielmehr um einen
teilelastischen Prozess: Es wird dabei nur ein Teil der Verformungsarbeit wieder
zurück in kinetische Energie gewandelt. Die Geschwindigkeiten der beteiligten
Gegenstände sind nach einem teilelastischen Stoß folglich kleiner als bei einem
elastischen Stoß.

Für die Bewegungsenergien :math:`E _{\rm{v}}` und :math:`E _{\rm{n}}` vor und
nach dem Stoß gilt:

.. math::
    
    \Delta E = (E _{\rm{v}} - E _{\rm{n}}) \cdot (1-k^2)

Die Zahl :math:`k` wird hierbei als Stoßzahl bezeichnet; sie kann mittels
folgender Formel experimentell bestimmt werden:

.. math::
    
    k = \frac{v_2 - v_1}{u_2 - u_1}

Die Stoßzahl :math:`k` ist gleich Null für komplett unelastische Prozesse und
gleich Eins für komplett elastische Prozesse. Für teilelastische Prozesse
ergibt sich eine Zahl zwischen Null und Eins, die den Elastizitätsgrad des
Prozesses angibt.


.. index:: Drehimpuls
.. _Drehimpuls:

Der Drehimpuls
--------------

In ähnlicher Weise, wie sich bei die Definition des Impulses der Beschreibung
von Translationsbewegungen als hilfreich herausgestellt hat, so hat sich auch
bei der Beschreibung von Rotationsbewegungen die Einführung eines so genannten
Drehimpulses als nützlich erwiesen.

Der Drehimpuls eines Körpers ist von seinem :ref:`Trägheitsmoment
<Trägheitsmoment>` und von seiner :ref:`Winkelgeschwindigkeit
<Winkelgeschwindigkeit>` abhängig und kennzeichnet die Wucht, die dieser Körper
bei einer Rotationsbewegung aufweist.

*Definition:*

    Der Drehimpuls :math:`\vec{L}` eines Körpers ist gleich dem Produkt aus seinem
    Trägheitsmoment :math:`J` und seiner Winkelgeschwindigkeit :math:`\vec{w}`:

    .. math::
        :label: eqn-drehimpuls
        
        \vec{L} = J \cdot \vec{w} 

..  Die Einheit des Impulses ist :math:`\unit[1]{kg \cdot \frac{m}{s}}`.

Der Drehimpuls ist eine vektorielle Größe und zeigt in die gleiche Richtung wie
die Winkelgeschwindigkeit, also senkrecht zur Drehebene. Der Betrag des
Drehimpuls eines rotierenden Körpers ändert sich, wenn sich entweder der Betrag
seiner Winkelgeschwindigkeit oder seine Massenverteilung und somit sein
Trägheitsmoment ändert. 

Mathematisch lässt sich die betragliche Änderung des Drehimpulses folgendermaßen
ausdrücken:

.. math::
    
    \Delta L = J \cdot \Delta \omega + \Delta J \cdot \omega{\color{white}\quad
    \;\;\; \ldots}

Diese Änderung des Impulses kann in Relation zur Zeit :math:`\Delta t` gesetzt
werden, in der die Änderung stattfindet. Damit folgt:

.. math::
    
    {\color{white}\ldots \qquad \qquad \quad   }\frac{\Delta L}{\Delta t} &=
    \frac{J \cdot \Delta \omega + \Delta J \cdot \omega}{\Delta t} = \frac{J
    \cdot \Delta \omega}{\Delta t} + \frac{\Delta J \cdot \omega}{\Delta t}
    \\[4pt]
    &= J \cdot \frac{\Delta \omega}{\Delta t} + \frac{\Delta J}{\Delta t} \cdot
    \omega

Der Term :math:`J \cdot \frac{\Delta \omega}{\Delta t}` im ersten Teil dieser
Summe kann aufgrund des Zusammenhangs :math:`\alpha = \frac{\Delta
\omega}{\Delta t}` auch als :math:`J \cdot \alpha` geschrieben werden. Dieser
Term kann als :ref:`Drehmoment <Drehmoment>` aufgefasst werden :math:`(M = J
\cdot \alpha)` und ist mit der Änderung des Drehimpulses identisch, sofern die
Änderung des Trägheitsmoments gleich Null ist. Andernfalls muss diese zusätzlich
berücksichtigt werden:

.. math::
    :label: eqn-drehimpuls-änderung
    
    {\color{white}\ldots}\vec{M} = \frac{\Delta \vec{L}}{\Delta t} = J \cdot
    \vec{\alpha} + \frac{\Delta J}{\Delta t} \cdot \vec{\omega}

Eine Drehmoment kann somit allgemein als zeitliche Änderung des Drehimpulses
aufgefasst werden. 

..  \vec{L} = \vec{p} \cdot \vec{d}

.. Mit d = Dreharm


.. _Drehimpulserhaltungssatz:

.. rubric:: Der Drehimpulserhaltungssatz

Ein System aus mehreren miteinander wechselwirkenden Körpern hat einen
Gesamt-Drehimpuls, welcher der Summe aller einzelnen Drehimpulse entspricht: 

.. math::
    :label: eqn-gesamt-drehimpuls
    
    \vec{L} _{\rm{ges}} = \sum_{i=1}^{n} J _{\rm{i}} \cdot \vec{\omega} _{\rm{i}} = J
    _{\rm{1}} \cdot \vec{\omega}_{\rm{1}} + J _{\rm{2}} \cdot \vec{\omega}_{\rm{2}} +
    \ldots + J _{\rm{n}} \cdot \vec{\omega}_{\rm{n}}

Wenn keine äußeren Drehmomente auf das System wirken, dann ist der
Gesamt-Drehimpuls konstant. Dieser empirisch gefundene Sachverhalt wird
Drehimpulserhaltung genannt und stellt gemeinsam mit der Impulserhaltung und der
Erhaltung der Energie einen der wichtigsten Erhaltungssätze der Mechanik dar.

.. raw:: latex

    Zu diesem Abschnitt gibt es Übungsaufgaben (Seite \pageref{Aufgaben
    zu Impuls und Drehimpuls}) und Versuche (Seite \pageref{Aufgaben zu Impuls
    und Drehimpuls})


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Nach der binomischen Formel ist :math:`v_1^2 - u_1^2 = (v_1 + u_1) \cdot
       (v_1 - u_1)`. Der letzte Term kann dabei gekürzt werden.

.. [#] Wie groß der Verlust an mechanischer Energie ist, kann aus der Differenz
    der :ref:`Bewegungsenergien <Kinetische Energie>` beider Kugeln vor und nach
    dem Stoß berechnet werden:

    .. math::
        
        \Delta E = \frac{1}{2} \cdot (m_1 \cdot v_1^2 + m_2 \cdot v_2^2 - (m_1 +
        m_2) \cdot u^2)
        
    Experimentell lässt sich ein unelastischer Stoß beispielsweise dadurch
    erreichen, dass an dem Berührungspunkt der Kugeln ein kleines Stück Kaugummi
    aufgeklebt wird.


