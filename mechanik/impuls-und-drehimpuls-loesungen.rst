.. _Lösungen Impuls und Drehimpuls:

Impuls und Drehimpuls
=====================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben
Impuls und Drehimpuls>` zum Abschnitt :ref:`Impuls und Drehimpuls <Impuls und
Drehimpuls>`.

----

.. _imp01l:

* Der Impuls :math:`\vec{p}` eines Körpers ist definiert als Produkt aus seiner Masse
  :math:`m` und seiner Geschwindigkeit :math:`\vec{v}`. Eine Taube mit einer
  Masse von :math:`m=\unit[20]{g} = \unit[0,02]{kg}` und einer Geschwindigkeit
  von :math:`v = \unit[75]{km/h} \approx \unit[20,8]{m/s}` hat somit folgenden
  Impuls:

  .. math::

      p = m \cdot v = \unit[0,02]{kg} \cdot \unit[20,8]{\frac{m}{s}} \approx
      \unit[0,42]{\frac{kg \cdot m}{s}}

  Der Impuls der Taube beträgt also rund :math:`\unit[0,42]{\frac{kg \cdot m}{s}}`

  :ref:`Zurück zur Aufgabe <imp01>`


----

.. _imp02l:

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

  :ref:`Zurück zur Aufgabe <imp02>`


----

.. _imp03l:

* Vor dem (unelastischen) Zusammenprall haben die beiden Fahrzeuge mit
  den Massen :math:`m_1 = \unit[1000]{kg}` und :math:`m_2 = \unit[2000]{kg}` und
  den Geschwindigkeiten :math:`v_1 = \unitfrac[50]{km}{h} =
  \unitfrac[13,9]{m}{s}` und :math:`v_2 = \unit[-50]{km}{h} =
  \unit[-13,9]{m}{s}` folgenden Gesamtimpuls:

  .. math::

      p = (m_1 \cdot v_2 + m_2 \cdot v_2) = \unit[1000]{kg} \cdot
      \unit[13,9]{\frac{m}{s}} + \unit[2000]{kg} \cdot
      (\unit[-13,9]{\frac{m}{s}}) = \unit[-13\,900]{\frac{kg \cdot m}{s}}

  ..
      50/3.6*1000   # pges

  Dieser Impuls bleibt nach dem Zusammenprall erhalten. Die Geschwindigkeit
  :math:`u`, mit der sich beide Fahrzeuge nach dem Stoß gemeinsam
  weiterbewegen, kann berechnet werden, wenn man den Gesamtimpuls durch die
  Gesamtmasse beider Fahrzeuge teilt:

  .. math::

      p = (m_1 + m_2) \cdot u \quad \Leftrightarrow \quad u = \frac{p}{m_1 +
      m_2} \\[4pt]

      \Rightarrow u = \frac{\unit[-13\,900]{\frac{kg \cdot
      m}{s}}}{\unit[1000]{kg} + \unit[2000]{kg}} \approx
      \unit[-4,63]{\frac{m}{s}}

  ..
      50/3.6*1000/3000  # vn

  Die beiden Fahrzeuge bewegen sich unmittelbar nach dem Stoß also gemeinsam mit
  rund :math:`\unitfrac[-4,63]{m}{s} \approx \unitfrac[16,7]{km}{h}` in Richtung des
  ersten (leichteren) Fahrzeugs.

  Der Fahrer des zweiten (schwereren) Fahrzeugs erfährt innerhalb des
  "Bremswegs" :math:`\Delta s = \unit[0,5]{m}` (der Knautschzone) eine
  Geschwindigkeitsänderung von :math:`|v_1| = \unitfrac[13,9]{m}{s}` auf
  :math:`|v|=\unitfrac[4,93]{m}{s}`. Damit kann man mittels der :ref:`Bremsformel
  <Bremsformel>` die wirkende Beschleunigung folgendermaßen berechnen:

  .. math::

      v^2 - v_2^2 = 2 \cdot a_2 \cdot \Delta s \quad \Longleftrightarrow \quad
      a_2 = \frac{v^2 - v_2^2}{2 \cdot \Delta s}\\[6pt]
      a_2 = \frac{\phantom{+}\unit[4,63^2]{\frac{m^2}{s^2}}  -
      \unit[13,9^2]{\frac{m^2}{s^2}}}{2 \cdot \unit[0,5]{m}} \approx
      \unit[-171,5]{\frac{m}{s^2}}

  ..
      -(50/3.6)**2 + (50/3.6*1000/3000)**2

  Der Fahrer des ersten (leichteren) Fahrzeugs wird innerhalb des gleichen
  Bremswegs :math:`\Delta s = \unit[0,5]{m}` (der Knautschzone des zweiten
  Fahrzeugs) nicht nur von der Geschwindigkeit :math:`v_1 =
  \unitfrac[+13,9]{m}{s}` bis zum Stillstand abgebremst, sondern zusätzlich
  auf :math:`\unitfrac[-4,63]{m}{s}` beschleunigt. In der Bremsformel kann dies
  explizit berücksichtigt werden, indem vor die Endgeschwindigkeit :math:`v` ein
  Minus-Zeichen gesetzt wird:

  .. math::

      a_1 = \frac{\unit[-4,63^2]{\frac{m^2}{s^2}} -
      \unit[13,9^2]{\frac{m^2}{s^2}}}{2 \cdot \unit[0,5]{m}} \approx
      \unit[-214,3]{\frac{m}{s^2}}

  ..
      -(50/3.6)**2 - (50/3.6*1000/3000)**2

  Die Bremsformel berücksichtigt aufgrund der Quadrierung der
  Geschwindigkeitswerte nicht die ursprüngliche Richtung der Geschwindigkeiten,
  sondern vergleicht lediglich die Beträge der Start- und Endgeschwindigkeit:
  Ist die Endgeschwindigkeit geringer als die Startgeschwindigkeit, so ergibt
  sich ein negatives Vorzeichen. Dies bedeutet hierbei nur, dass die
  Beschleunigung entgegen der bisherigen Bewegungsrichtung verläuft; die
  physikalische Interpretation, ob die Beschleunigung "nach links" oder "nach
  rechts" gerichtet ist, muss man hingegen selbst treffen.

  An den Beträgen der Beschleunigungen kann man erkennen, dass der Fahrer des
  schwereren Fahrzeugs beim Zusammenstoß eine geringere Bremsbeschleunigung
  erfährt der Fahrer des leichten Fahrzeugs; er hat also eine höhere
  Überlebenswahrscheinlichkeit.

  Leichte Fahrzeuge gefährden zwar andere Verkehrsteilnehmer nur in geringerem
  Maße, sind aber bei Verkehrsunfällen gegenüber schweren Fahrzeugen
  benachteiligt. "Fair-Play"-Regelungen, wonach beispielsweise für schwere
  Fahrzeuge entsprechend striktere Regeln bezüglich Knautschzonen gelten
  müssten, konnten sich politisch bislang leider nicht durchsetzen.

.. Jeder Zentner Mehrgewicht kostet im Schnitt 0,2 Liter Kraftstoff auf 100
.. Kilometer.

  :ref:`Zurück zur Aufgabe <imp03>`

----

.. foo

.. only:: html

    :ref:`Zurück zum Skript <Impuls und Drehimpuls>`

