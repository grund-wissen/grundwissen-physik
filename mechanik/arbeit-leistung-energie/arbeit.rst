.. meta::
   :description: Mechanische Arbeit
   :keywords: Arbeit, Joule

.. index:: Arbeit
.. _Mechanische Arbeit:

Die mechanische Arbeit
======================

Wirkt eine Kraft auf einen Körper ein und bewirkt dabei eine Verformung, eine
Beschleunigung oder ein Anheben des Körpers, so wird physikalische Arbeit
verrichtet. Um die Größe der verrichteten Arbeit zu bestimmen, müssen der Betrag
der Kraft und die Länge des Weges, entlang dessen die Kraft wirkt, bekannt sein.

*Definition:*

    Die Arbeit :math:`W` ist das Produkt aus der in Richtung des Weges wirkenden
    Kraft :math:`F` und der zurückgelegten Wegstrecke :math:`s`: [#]_

.. math::
    :label: eqn-arbeit

    W = F \cdot s _{\rm{\parallel}}

.. Wenn \alpha Winkel zwischen Kraftrichtung und Wegrichtung :math:`(0 < \alpha < 90 \degree)`, so W = F \cdot s \cdot \cos{\alpha}

..
    Wenn Kraft nicht konstant, sondern Funktion des Weges s, und stehen
    gegebenenfalls Kraft und Weg im Winkel \alpha zueinander, so ist die Arbeit
    gleich dem Integral ueber :math:`F(s)`.

    .. math::

        W = \int_{s_1}^{s^2} F  \cdot  \cos{\alpha} \cdot \mathrm{d} s

    In einem F-S-Diagramm entspricht die verrichtete Arbeit der Flaeche
    unterhalb der Kurve von :math:`F(s)`.


*Einheit:*

    Die Einheit der Arbeit ist nach Gleichung :eq:`eqn-arbeit` das Produkt der
    Einheiten von Kraft und Weg. Sie wird zu Ehren des Physikers `James Prescott
    Joule <http://de.wikipedia.org/wiki/James_Prescott_Joule>`_ kurzerhand Joule
    :math:`\unit[]{(J)}` genannt.

.. math::

    \unit[1]{J} = \unit[1]{N } \cdot \unit[1]{m}

*Beispiele:*

* Die Gewichtskraft :math:`F _{\rm{G}}` einer Tafel Schokolade :math:`( m =
  \unit[100]{g})` entspricht in guter Näherung :math:`\unit[1]{N}`. Hebt man
  eine Tafel Schokolade einen Meter weit an (egal von welcher Position aus), so
  verrichtet man dabei eine Arbeit von :math:`W = F _{\rm{G}} \cdot s =
  \unit[1]{N} \cdot \unit[1]{m} = \unit[1]{J}`.

* Hebt man :math:`2, 3, 4, \ldots`  Tafeln Schokolade einen Meter weit an, so
  verrichtet man entsprechend eine Arbeit von :math:`\unit[2, 3, 4, \ldots]{J}`.
  Mit der gleichen Arbeit könnte man jeweils auch *eine* Tafel Schokolade um
  :math:`\unit[2, 3, 4, \ldots]{m}` anheben.

* Um zwei Tafeln Schokolade zwei Meter weit anzuheben, muss man eine Arbeit von
  :math:`\unit[2]{N} \cdot \unit[2]{m} = \unit[4]{N \cdot m} = \unit[4]{J}`
  verrichten.

Unter der Bedingung, dass die Kraft konstant ist und in beliebiger, aber fester
Richtung wirkt, gilt:

.. math::

    W = F \cdot s \cdot \cos{\alpha }


.. _Arten mechanischer Arbeit:

Arten mechanischer Arbeit
-------------------------

Bei mechanischen Prozessen ist sind die folgenden Arten mechanischer Arbeit von
entscheidender Bedeutung:

.. index::
    single: Arbeit; Hubarbeit
.. _Hubarbeit:

.. rubric:: Die Hubarbeit

Erfahrungsgemäß ist es einfacher, einen leichten Körper hoch zu heben als einen
schweren. Doch auch beim Heben zweier gleich schwerer Körper gibt es
Unterschiede: Je weiter man einen Körper hoch heben muss, desto mehr Arbeit ist
dafür nötig.

*Definition:*

    Die Hubarbeit :math:`W _{\rm{Hub}}` ist proportional zur :ref:`Gewichtskraft
    <Gewichtskraft>` :math:`F _{\rm{ G}}` eines angehobenen Körpers und zur
    Hubhöhe :math:`h`:

.. math::
    :label: eqn-hubarbeit

    W _{\rm{Hub}} = F _{\rm{G}} \cdot h

Die Hubarbeit kann mit Hilfe der Formel für die Gewichtskraft (:math:`F _{\rm{G}} = m
\cdot g`) auch als :math:`W _{\rm{Hub}} = m \cdot g \cdot h` geschrieben werden.


.. index::
    single: Arbeit; Reibungsarbeit
.. _Reibungsarbeit:

.. rubric:: Die Reibungsarbeit

Um einen Körper auf einer waagrechten Ebene gleichförmig zu bewegen, muss der
Reibungskraft eine gleich große Gegenkraft entgegenwirken.

*Definition:*

    Die Reibungsarbeit :math:`W _{\rm{Reib}}` ist proportional zur
    :ref:`Reibungskraft <Reibungskraft>` :math:`F _{\rm{R}}` und zur
    zurückgelegten Wegstrecke :math:`s`:

.. math::
    :label: eqn-reibungsarbeit

    W _{\rm{Reib}} = F _{\rm{R}} \cdot s

Beim gleichzeitigen Auftreten mehrerer Reibungskräfte (z.B. Rollreibung und
Luftwiderstand) entspricht :math:`F _{\rm{R}}` der Summe aller auftretenden
Reibungskräfte.


.. index::
    single: Arbeit; Spannarbeit
.. _Spannarbeit:

.. rubric:: Die Spannarbeit

Die Spannkraft, die ein elastischer Körper (z.B. eine Schraubenfeder) einer
Stauchung oder Streckung entgegensetzt, ist nicht konstant, sondern nimmt
gleichmäßig mit der Auslenkung zu:

* Die anfängliche Spannkraft der Feder in der Ruhelage ist Null.
* Wird die Feder um eine Wegstrecke :math:`s` ausgelenkt, so beträgt die
  :ref:`Spannkraft <Spannkraft>` der Feder :math:`F _{\rm{S}} = -k \cdot s`.


Entlang der Strecke :math:`s` muss im Durchschnitt nur die Hälfte der
(maximalen) Spannkraft :math:`F _{\rm{S}}` am Auslenkungspunkt aufgewendet
werden. Für die durchschnittlich nötige Kraft :math:`\bar{F}_{\rm{S}}` gilt
also:

.. math::

    \bar{F} _{\rm{S}} = \frac{1}{2} \cdot F _{\rm{s}}

Dies gilt allgemein für elastische Verformungen.

*Definition:*

    Die zur Verformung eines elastischen Körpers (z.B. einer Schraubenfeder)
    nötige Spannarbeit :math:`W _{\rm{Spann}}` ist proportional zur
    durchschnittlichen Spannkraft :math:`\bar{F} _{\rm{S}} = \frac{1}{2} \cdot F
    _{\rm{S}}` und der dazugehörigen Auslenkung :math:`s`:

.. math::
    :label: eqn-spannarbeit

    W _{\rm{Spann}} = \bar{F} _{\rm{S}} \cdot s = \frac{1}{2} \cdot F _{\rm{S}} \cdot s

Die Spannarbeit kann mit Hilfe der Formel für die Spannkraft (:math:`F _{\rm{S}}
= - D \cdot s`) auch als :math:`W _{\rm{Spannn}} = \frac{1}{2} \cdot D \cdot
s^2` geschrieben werden, wobei :math:`D` die (oftmals experimentell zu
bestimmende) Federkonstante des Körpers angibt.


.. index::
    single: Arbeit; Beschleunigungsarbeit
.. _Beschleunigungsarbeit:

.. rubric:: Die Beschleunigungsarbeit

Zur Überwindung der Trägheit ist eine Kraft notwendig. Die zugehörige Arbeit,
die bei einer Beschleunigung entlang einer Strecke :math:`s`  auftritt, heißt
Beschleunigungsarbeit.

*Definition:*

    Die Beschleunigungsarbeit :math:`W _{\rm{B}}` eines zunächst ruhenden
    Körpers der Masse :math:`m` ist proportional zum Quadrat der
    Endgeschwindigkeit :math:`v`, die dieser erreicht: [#]_

.. math::
    :label: eqn-beschleunigungsarbeit

    W _{\rm{B}} = \frac{1}{2} \cdot m \cdot v^2

Besitzt der Körper bereits eine Anfangsgeschwindigkeit :math:`v _{\rm{1}}` und
wird auf eine Endgeschwindigkeit :math:`v _{\rm{2}}` beschleunigt, so beträgt
die Beschleunigungsarbeit :math:`W _{\rm{B}} = \frac{1}{2} \cdot m \cdot (v_2^2
- v_1^2)`.


.. index::
    single: Arbeit; Rotationsarbeit
.. _Rotationsarbeit:

.. rubric:: Die Rotationsarbeit

Zur Überwindung der Trägheit ist für eine Rotation eine Drehmoment notwendig.
Die zugehörige Arbeit heißt Rotationsarbeit.

*Definition:*

    Die Rotationsarbeit :math:`W _{\rm{rot}}` eines zunächst ruhenden Körpers
    mit :ref:`Trägheitsmoment <Trägheitsmoment>` :math:`J` ist proportional zum
    Quadrat der :ref:`Winkelgeschwindigkeit <Winkelgeschwindigkeit>`
    :math:`\omega`, die dieser erreicht:

.. math::
    :label: eqn-rotationsarbeit

    W _{\rm{rot}} = \frac{1}{2} \cdot J \cdot \omega^2

Besitzt der Körper bereits eine Anfangsgeschwindigkeit :math:`\omega _{\rm{1}}`
und wird auf eine Endgeschwindigkeit :math:`\omega _{\rm{2}}` beschleunigt, so
muss in Gleichung :eq:`eqn-rotationsarbeit` anstelle :math:`\omega` die
Differenz :math:`\Delta \omega = \omega _{\rm{2}} - \omega _{\rm{1}}` beider
Winkelgeschwindigkeiten eingesetzt werden.

.. Rotationsarbeit \Delta W _{\rm{rot}} = M \cdot \Delta \varphi = J \cdot \alpha \cdot \Delta \varphi
.. = J \cdot (\frac{\Delta \omega}{\Delta t}) \cdot \Delta \varphi
.. = J \cdot (\frac{1}{2} \cdot \frac{\Delta \varphi}{\Delta t^2}) \cdot \Delta \varphi
.. = J \cdot (\frac{1}{2} \cdot \frac{\Delta \varphi^2}{\Delta t^2})
.. = J \cdot \frac{1}{2} \cdot \omega^2


.. _Goldene Regel der Mechanik:

Die goldene Regel der Mechanik
------------------------------

Während Kräfte durch entsprechende Hilfsmittel in ihrer Richtung oder ihrem
Betrag geändert werden können, kann die für einen mechanischen Prozess nötige
Arbeit nicht verringert werden; die Menge an Arbeit bleibt erhalten.

Bei Verwendung eines Kraftwandlers ist die aufgenommene Arbeit stets gleich der
abgegebenen Arbeit (Reibung wird vernachlässigt):

.. math::

    F_1 \cdot s_1 &= F_2 \cdot s_2 \\[6pt]
    W_1 &= W_2

Abgesehen von Reibungsverlusten bleibt das Produkt aus Weg und Kraft (entlang
des Weges) stets konstant. Eine umgangssprachliche Formulierung für das Prinzip
der Kraftwandlung ("die goldene Regel der Mechanik") lautet daher:

.. centered:: "Was an Kraft eingespart wird, muss an Weg zugesetzt werden."

*Beispiele:*

* Bei einer :ref:`festen Rolle <Feste Rolle>` ist die zum Heben aufgewendete Kraft
  :math:`F_1` gleich der wirksamen Kraft :math:`F_2`. Der Weg der Kraft
  :math:`F_1` ist gleich dem Weg der Kraft :math:`F_2`. Somit gilt:

  .. math::

      F_1 \cdot s_1 = F_2 \cdot s_2

* Bei einer :ref:`losen Rolle <Lose Rolle>` ist die zum Heben aufgewendete Kraft
  :math:`F_1` gleich der Hälfte der wirksamen Kraft :math:`F_2`. Der Weg der
  Kraft :math:`F_1` ist allerdings doppelt so groß wie der Weg der Kraft
  :math:`F_2`. Insgesamt gilt:

  .. math::

      F_1 &= \frac{1}{2} \cdot F_2{\color{white}\ldots} \\
      s_1 &= 2 \cdot s_2 \\
      \Rightarrow F_1 \cdot s_1 = \frac{1}{2} \cdot F_2 &\, \cdot \, 2 \cdot s_2 = F_2 \cdot s_2

* Um einen Körper mit einer Gewichtskraft :math:`F _{\rm{G}}` auf eine Höhe
  :math:`h` zu heben, ist die Hubarbeit :math:`W _{\rm{Hub}} = F _{\rm{G}} \cdot
  h` nötig. Verschiebt man ihn hingegen entlang des längeren Weges :math:`l`
  einer :ref:`schiefen Ebene <Schiefe Ebene>` nach oben, so ist die nötige
  Kraft :math:`F` um das Verhältnis :math:`\frac{h}{l}` geringer. Es gilt:

  .. math::

      F \cdot l = F _{\rm{G}} \cdot h


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die Arbeits-Formel :math:`W = F \cdot s` gilt streng genommen nur, wenn
    die wirkende Kraft F konstant ist. Ist die Kraft nur innerhalb einzelner
    Zeitabschnitte konstant, so muss man die Formel für jeden dieser
    Zeitabschnitte einzeln anwenden und die jeweiligen Teilbeträge summieren.

    .. math::

        W = \sum_{i}^{} F  _{\rm{i}} \cdot s _{\rm{i}}

    Im Fall einer sich kontinuierlich ändernden Kraft wird aus der Summe
    :math:`(\sum_{}^{})` ein Integral :math:`(\int_{}^{})`.

.. [#]  Um die Formel für die Beschleunigungsarbeit :math:`W _{\rm{B}}`
    herzuleiten, geht man von der allgemeinen Definition der Arbeit :math:`W = F
    \cdot s` aus. Für die Kraft :math:`F` kann man das allgemeine Kraftgesetz
    :math:`F = m \cdot a` einsetzen. Für die Wegstrecke kann man die
    :ref:`Bremsformel <Bremsformel>` :math:`v^2-v_0^2 = 2 \cdot a \cdot s` nach
    :math:`s` auflösen. Erfolgt die Beschleunigung aus dem Stillstand
    :math:`(v_0=0)`, so ist :math:`s = \frac{v^2}{2 \cdot a}`. Setzt man
    auch diesen Ausdruck in die allgemeine Definition der Arbeit ein, so erhält
    man:

    .. math::

        W _{\rm{B}} = F \cdot s =  (m \cdot a)  \cdot \frac{v^2}{2 \cdot a} =
        \frac{1}{2} \cdot m \cdot v^2

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Versuche <Versuche zu mechanischer Arbeit>` und
    :ref:`Übungsaufgaben <Aufgaben zu mechanischer Arbeit>`.


