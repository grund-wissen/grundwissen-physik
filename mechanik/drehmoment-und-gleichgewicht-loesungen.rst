
.. _Lösungen zu Drehmoment und Gleichgewicht:

.. only:: html

Lösungen zu Drehmoment und Gleichgewicht
========================================

Die folgenden Lösungen beziehen sich auf die :ref:`Übungsaufgaben <Aufgaben zu
Drehmoment und Gleichgewicht>` zum Abschnitt :ref:`Drehmoment und Gleichgewicht
<Drehmoment und Gleichgewicht>`.

----

.. _Gleichgewicht-01-Lösung:

* Die Standfestigkeit eines Körpers ist umso größer, je größer seine Masse und
  Standfläche und je tiefer sein Schwerpunkt ist.

  :ref:`Zurück zur Aufgabe <Gleichgewicht-01>`

----

.. _Gleichgewicht-02-Lösung:

* Während die Last getragen wird, ist sie im statischen Gleichgewicht; das
  heißt, die an ihr angreifenden Kräfte und Drehmomente ergeben in Summe jeweils
  Null. Betrachtet man zunächst nur den Einfluss
  :math:`F_{\mathrm{G}}=\unit[120]{N}` der Last, so gilt:

  .. math::

      F_1 + F_2 - F_{\mathrm{G}} &= 0 \\
      - F_1 \cdot s_1 + F_2 \cdot s_2 &= 0 \\

  Die erste Gleichung ergibt sich daraus, dass die beiden von den Trägern
  ausgeübten Kräfte das Gewicht der Last ausgleichen, die Last also nicht nach
  unten sinkt. Die zweite Gleichung erhält man, wenn man sich jeweils einen der
  beiden Träger "weggeschnitten" denkt; das Brett mitsamt Last würde dann
  kippen, wobei die Drehachse mit der Hand des verbliebenen Trägers identisch
  wäre. An der Stelle des jeweils "weggeschnittenen" Trägers muss also eine
  Kraft wirken, die das von der Last bewirkte Drehmoment ausgleicht.

  .. figure:: 
      ../pics/mechanik/drehmoment-und-gleichgewicht/gewichtsverteilung-loesung.png
      :align: center
      :width: 70%

  .. only:: html

      .. centered:: :download:`SVG: Gewichtsverteilung (Lösung) <../pics/mechanik/drehmoment-und-gleichgewicht/gewichtsverteilung-loesung.svg>`


  Aus der zweiten der obigen Gleichungen folgt:

  .. math::

      F_1 \cdot s_1 &= - F_2 \cdot s_2 \\
      \Rightarrow \; \frac{F_1}{F_2} = - \frac{s_2}{s_1}

  Die von den beiden Trägern aufzubringenden Kräfte stehen also im umgekehrten
  Verhältnis zu den jeweiligen Entfernungen der Last von den beiden Trägern. Das
  Vorzeichen ergibt sich daraus, dass die Wegstrecke :math:`s_2` in die
  umgekehrte Richtung zeigt wie :math:`s_1`; da linksdrehende Drehmomente
  definitionsgemäß als positiv und rechtsdrehende Drehmomente definitionsgemäß
  als positiv gezählt werden, erhält in diesem Fall :math:`s_1` ein negatives
  Vorzeichen. Mit :math:`s_1 = \unit[1]{m}` und :math:`s_2 = \unit[-2]{m}` folgt
  also :math:`F_1 = 2 \cdot F_2`.

  Setzt man dieses Zwischenergebnis in die erste der obigen Gleichungen ein, so
  erhält man:

  .. math::

      F_1 + F_2 &= F_{\mathrm{G}} \\
      (2 \cdot F_2) + F_2 &= F_{\mathrm{G}} \\
      F_2 &= \frac{F_{\mathrm{G}}}{3} = \frac{\unit[120]{N}}{3} = \unit[40]{N}\\

  Der hintere Träger muss zum Heben der Last somit die Kraft :math:`F_1 =
  \unit[80]{N}`, der vordere Träger die Kraft :math:`F_2 = \unit[40]{N}`
  aufbringen. Zusätzlich müssen beide Träger weitere :math:`\unit[10]{N}` zum
  Heben des Brettes aufbringen; dessen Gewicht verteilt sich nämlich (nach dem
  gleichen Prinzip) gleichmäßig auf beide Träger, da sich sein Schwerpunkt in
  der Mitte zwischen den beiden Personen befindet.


  :ref:`Zurück zur Aufgabe <Gleichgewicht-02>`


.. raw:: latex

    \rule{\linewidth}{0.5pt}

.. raw:: html

    <hr/>

.. only:: html

    :ref:`Zurück zum Skript <Drehmoment und Gleichgewicht>`

