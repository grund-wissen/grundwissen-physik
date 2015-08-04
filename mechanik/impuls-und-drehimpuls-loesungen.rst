.. _Lösungen zu Impuls und Drehimpuls:

Lösungen zu Impuls und Drehimpuls
=================================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben zu
Impuls und Drehimpuls>` zum Abschnitt :ref:`Impuls und Drehimpuls <Impuls und
Drehimpuls>`.

----

.. _Impuls-01-Lösung:

* Der Impuls :math:`\vec{p}` eines Körpers ist definiert als Produkt aus seiner Masse
  :math:`m` und seiner Geschwindigkeit :math:`\vec{v}`. Eine Taube mit einer
  Masse von :math:`m=\unit[20]{g} = \unit[0,02]{kg}` und einer Geschwindigkeit
  von :math:`v = \unit[75]{km/h} \approx \unit[20,8]{m/s}` hat somit folgenden
  Impuls:

  .. math::
      
      p = m \cdot v = \unit[0,02]{kg} \cdot \unit[20,8]{\frac{m}{s}} \approx
      \unit[0,42]{\frac{kg \cdot m}{s}}

  Der Impuls der Taube beträgt also rund :math:`\unit[0,42]{\frac{kg \cdot m}{s}}`

  :ref:`Zurück zur Aufgabe <Impuls-01>`


----

.. _Impuls-02-Lösung:

* Wenn der Eisenbahnwagen an die stehenden Wagen ankoppelt, bewegen sie sich, --
  wie bei jedem unelastischen Stoß -- anschließend mit einer gemeinsamen
  Geschwindigkeit :math:`u` weiter. Diese kann mit Hilfe des
  Impulserhaltungs-Satzes bestimmt werden.

  Vor dem Stoß bewegt sich nur einer der Wagen mit einer Geschwindigkeit
  :math:`v_1=\unit[3]{m/s}` und einer Masse :math:`m_1`. Nach dem Stoß bewegen
  sich alle vier Wagen der Geschwindigkeit Geschwindigkeit :math:`u`, ihre Masse
  ist dabei :math:`m = 4 \cdot m_1`. Da der Gesamt-Impuls vor und nach dem Stoß
  identisch ist, muss somit gelten:

  .. math::
      
      m_1 \cdot v_1 = 4 \cdot m_1 \cdot u \quad \Leftrightarrow \quad u =
      \frac{1}{4} \cdot v_1
  
  Die Wagen bewegen sich nach dem Ankoppeln also gemeinsam mit :math:`u =
  \unit[0,75]{m/s}` weiter.
  
  :ref:`Zurück zur Aufgabe <Impuls-02>`


----

.. _Impuls-03-Lösung:

* Vor dem (unelastischen) Zusammenprall haben die beiden Fahrzeuge mit
  den Massen :math:`m_1 = \unit[1000]{kg}` und :math:`m_2 = \unit[2000]{kg}` und
  den Geschwindigkeiten :math:`v_1 = \unit[50]{km/h} = \unit[13,9]{m/s}` und
  :math:`v_2 = \unit[-50]{km/h} = \unit[-13,9]{m/s}` folgenden Gesamtimpuls:

  .. math::
      
      p = (m_1 \cdot v_2 + m_2 \cdot v_2) = \unit[1000]{kg} \cdot
      \unit[13,9]{\frac{m}{s}} + \unit[2000]{kg} \cdot (\unit[-13,9]{\frac{m}{s}})
      = - \unit[13\,900]{\frac{kg \cdot m}{s}}

  Dieser Impuls bleibt nach dem Zusammenprall erhalten. Die Geschwindigkeit
  :math:`u`, mit der sich beide Fahrzeuge nach dem Stoß gemeinsam
  weiterbewegen, kann berechnet werden, wenn man den Gesamtimpuls durch die
  Gesamtmasse beider Fahrzeuge teilt:

  .. math::
      
      p = (m_1 + m_2) \cdot u \quad \Leftrightarrow \quad u = \frac{p}{m_1 + m_2} \\[4pt]

      \Rightarrow u = \frac{\unit[-13\,900]{\frac{kg \cdot
      m}{s}}}{\unit[1000]{kg} + \unit[2000]{kg}} \approx
      \unit[-4,63]{\frac{m}{s}}

  Die beiden Fahrzeuge bewegen sich unmittelbar nach dem Stoß also mit rund
  :math:`\unit[4,63]{m/s} \approx \unit[16,7]{km/h}` in Richtung des leichteren
  Fahrzeugs. 
  
  Der Fahrer des leichteren Fahrzeugs erfährt somit innerhalb eines "Bremswegs"
  von :math:`\Delta s = \unit[0,5]{m}` (der Knautschzone) eine
  Geschwindigkeitsänderung :math:`\unit[+50]{km/h}` auf
  :math:`\unit[-16,7]{km/h}`, das heißt :math:`\Delta v_1 = \unit[-67,7]{km/h}
  \approx \unit[18,5]{m/s}`. Entsprechend beträgt die
  Geschwindigkeitsänderung, die der Fahrer des schweren Fahrzeugs erfährt,
  :math:`\Delta v_2 = \unit[+16,7]{km/h} - \unit[50]{km/h} = \unit[33,3]{km/h}
  \approx \unit[9,3]{m/s}`. Für die beiden Beschleunigungen :math:`a_1` und
  :math:`a_2` gilt damit (vergleiche Aufgabe :ref:`"Gegen die Wand"
  <Beschleunigung-06>`):
  
  .. math::
      
      - v_1^2 = 2 \cdot a_2 \cdot s \quad &\Leftrightarrow \quad a_1 =
        \frac{-v_1^2}{2 \cdot s} \\[4pt]
      a_1 =  \frac{-\left( \unit[18,5]{\frac{m}{s}} \right)^2}{2 \cdot
      \unit[0,5]{m}} &\approx - \unit[343]{\frac{m}{s^2}} \approx 35 \cdot g
      \\[10pt]

      - v_2^2 = 2 \cdot a_2 \cdot s \quad &\Leftrightarrow \quad a_2 =
        \frac{-v_1^2}{2 \cdot s} \\[4pt]
      a_2 =  \frac{-\left( \unit[9,3]{\frac{m}{s}} \right)^2}{2 \cdot
      \unit[0,5]{m}} &\approx - \unit[86]{\frac{m}{s^2}} \approx 9 \cdot g

  Werden beide Karosserien als gleich stabil angenommen, so erfährt der Fahrer
  des schwereren Fahrzeugs beim Zusammenstoß somit etwa eine (noch überlebbare)
  neunfache Erdbeschleunigung, der Fahrer des leichten Fahrzeugs hingegen eine
  etwa (in den meisten Fällen tödliche) 35-fache Erdbeschleunigung. 
  
  Um den gleiche Beschleunigungsverhältnis zu erzielen, müsste das leichtere
  Fahrzeug frontal mit einem gleich schweren, aber doppelt so schnellen Fahrzeug
  frontal zusammenprallen. Leichtere Fahrzeuge sind also, obwohl sie meist
  umweltfreundlicher sind, bei Verkehrsunfällen benachteiligt. Leider konnten
  sich "Fair-Play"-Regelungen, wonach für schwere Fahrzeuge striktere Regeln
  bezüglich Knautschzonen gelten müssen, bislang nicht durchsetzen..

..  Jeder Zentner Mehrgewicht kostet im Schnitt 0,2 Liter Kraftstoff auf 100 Kilometer. 

  :ref:`Zurück zur Aufgabe <Impuls-03>`

.. raw:: latex

    \rule{\linewidth}{0.5pt}

.. raw:: html

    <hr/>
    
.. only:: html

    :ref:`Zurück zum Skript <Impuls und Drehimpuls>`

