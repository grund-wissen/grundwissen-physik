.. meta::
   :description: Mechanische Arbeit
   :keywords: Arbeit, Joule (Einheit)

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

    W = F \cdot s_{\mathrm{\parallel}}

.. Wenn \alpha Winkel zwischen Kraftrichtung und Wegrichtung :math:`(0 < \alpha
.. < 90 \degree)`, so W = F \cdot s \cdot \cos{\alpha}

    .. math::

        W = \int_{s_1}^{s^2} F  \cdot  \cos{\alpha} \cdot \mathrm{d} s

    In einem :math:`F(s)`-Diagramm entspricht die zwischen zwei Punkten
    :math:`s_1` und :math:`s_2` verrichtete Arbeit der Fläche zwischen dem
    entsprechenden Abschnitt des Graphen und der horizontalen :math:`s`-Achse.


*Einheit:*

    Die Einheit der Arbeit ist nach Gleichung :eq:`eqn-arbeit` das Produkt der
    Einheiten von Kraft und Weg. Sie wird nach `James Prescott Joule
    <https://de.wikipedia.org/wiki/James_Prescott_Joule>`_ kurzerhand Joule
    :math:`\unit[]{(J)}` genannt.

.. math::

    \unit[1]{J} = \unit[1]{N } \cdot \unit[1]{m}

*Beispiele:*

* Die Gewichtskraft :math:`F_{\mathrm{G}}` einer Tafel Schokolade :math:`( m =
  \unit[100]{g})` entspricht in guter Näherung :math:`\unit[1]{N}`. Hebt man
  eine Tafel Schokolade einen Meter weit an (egal von welcher Position aus), so
  verrichtet man dabei eine Arbeit von :math:`W = F_{\mathrm{G}} \cdot s =
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

.. index:: Arbeit; Hubarbeit
.. _Hubarbeit:

.. rubric:: Die Hubarbeit

Erfahrungsgemäß ist es einfacher, einen leichten Körper hoch zu heben als einen
schweren. Doch auch beim Heben zweier gleich schwerer Körper gibt es
Unterschiede: Je weiter man einen Körper hoch heben muss, desto mehr Arbeit ist
dafür nötig.

*Definition:*

    Die Hubarbeit :math:`W_{\mathrm{Hub}}` ist proportional zur
    :ref:`Gewichtskraft <Gewichtskraft>` :math:`F_{\mathrm{ G}}` eines
    angehobenen Körpers und zur Hubhöhe :math:`h`:

.. math::
    :label: eqn-hubarbeit

    W_{\mathrm{Hub}} = F_{\mathrm{G}} \cdot h

Die Hubarbeit kann mit Hilfe der Formel für die Gewichtskraft
(:math:`F_{\mathrm{G}} = m \cdot g`) auch als :math:`W_{\mathrm{Hub}} = m \cdot
g \cdot h` geschrieben werden.


.. index:: Arbeit; Reibungsarbeit
.. _Reibungsarbeit:

.. rubric:: Die Reibungsarbeit

Um einen Körper auf einer waagrechten Ebene gleichförmig zu bewegen, muss der
Reibungskraft eine gleich große Gegenkraft entgegenwirken.

*Definition:*

    Die Reibungsarbeit :math:`W_{\mathrm{Reib}}` ist proportional zur
    :ref:`Reibungskraft <Reibungskraft>` :math:`F_{\mathrm{R}}` und zur
    zurückgelegten Wegstrecke :math:`s`:

.. math::
    :label: eqn-reibungsarbeit

    W_{\mathrm{Reib}} = F_{\mathrm{R}} \cdot s

Beim gleichzeitigen Auftreten mehrerer Reibungskräfte (beispielsweise
Rollreibung und Luftwiderstand) entspricht :math:`F_{\mathrm{R}}` der Summe
aller auftretenden Reibungskräfte.


.. index:: Arbeit; Spannarbeit
.. _Spannarbeit:

.. rubric:: Die Spannarbeit

Die Spannkraft, die ein elastischer Körper (beispielsweise eine Schraubenfeder) einer
Stauchung oder Streckung entgegensetzt, ist nicht konstant, sondern nimmt
gleichmäßig mit der Auslenkung zu:

* Die anfängliche Spannkraft der Feder in der Ruhelage ist Null.
* Wird die Feder um eine Wegstrecke :math:`s` ausgelenkt, so beträgt die
  :ref:`Spannkraft <Spannkraft>` der Feder :math:`F_{\mathrm{S}} = -k \cdot s`.


Entlang der Strecke :math:`s` muss im Durchschnitt nur die Hälfte der
(maximalen) Spannkraft :math:`F_{\mathrm{S}}` am Auslenkungspunkt aufgewendet
werden. Für die durchschnittlich nötige Kraft :math:`\bar{F}_{\mathrm{S}}` gilt
also:

.. math::

    \bar{F} _{\mathrm{S}} = \frac{1}{2} \cdot F_{\mathrm{s}}

Dies gilt allgemein für elastische Verformungen.

*Definition:*

    Die zur Verformung eines elastischen Körpers (beispielsweise einer
    Schraubenfeder) nötige Spannarbeit :math:`W_{\mathrm{Spann}}` ist
    proportional zur durchschnittlichen Spannkraft :math:`\bar{F} _{\mathrm{S}}
    = \frac{1}{2} \cdot F_{\mathrm{S}}` und der dazugehörigen Auslenkung
    :math:`s`:

.. math::
    :label: eqn-spannarbeit

    W_{\mathrm{Spann}} = \bar{F} _{\mathrm{S}} \cdot s = \frac{1}{2} \cdot
    F_{\mathrm{S}} \cdot s

Die Spannarbeit kann mit Hilfe der Formel für die Spannkraft
(:math:`F_{\mathrm{S}} = - D \cdot s`) auch als :math:`W_{\mathrm{Spannn}} =
\frac{1}{2} \cdot D \cdot s^2` geschrieben werden, wobei :math:`D` die (oftmals
experimentell zu bestimmende) Federkonstante des Körpers angibt.


.. index:: Arbeit; Beschleunigungsarbeit
.. _Beschleunigungsarbeit:

.. rubric:: Die Beschleunigungsarbeit

Zur Überwindung der Trägheit ist eine Kraft notwendig. Die zugehörige Arbeit,
die bei einer Beschleunigung entlang einer Strecke :math:`s`  auftritt, heißt
Beschleunigungsarbeit.

*Definition:*

    Die Beschleunigungsarbeit :math:`W_{\mathrm{B}}` eines zunächst ruhenden
    Körpers der Masse :math:`m` ist proportional zum Quadrat der
    Endgeschwindigkeit :math:`v`, die dieser erreicht: [#]_

.. math::
    :label: eqn-beschleunigungsarbeit

    W_{\mathrm{B}} = \frac{1}{2} \cdot m \cdot v^2

Besitzt der Körper bereits eine Anfangsgeschwindigkeit :math:`v_1` und wird auf
eine Endgeschwindigkeit :math:`v_2` beschleunigt, so beträgt die
Beschleunigungsarbeit :math:`W_{\mathrm{B}} = \frac{1}{2} \cdot m \cdot (v_2^2 -
v_1^2)`.


.. index:: Arbeit; Rotationsarbeit
.. _Rotationsarbeit:

.. rubric:: Die Rotationsarbeit

Zur Überwindung der Trägheit ist für eine Rotation eine Drehmoment notwendig.
Die zugehörige Arbeit heißt Rotationsarbeit.

*Definition:*

    Die Rotationsarbeit :math:`W_{\mathrm{rot}}` eines zunächst ruhenden Körpers
    mit :ref:`Trägheitsmoment <Traegheitsmoment>` :math:`J` ist proportional zum
    Quadrat der :ref:`Winkelgeschwindigkeit <Winkelgeschwindigkeit>`
    :math:`\omega`, die dieser erreicht:

.. math::
    :label: eqn-rotationsarbeit

    W_{\mathrm{rot}} = \frac{1}{2} \cdot J \cdot \omega^2

Besitzt der Körper bereits eine Anfangsgeschwindigkeit :math:`\omega_1`
und wird auf eine Endgeschwindigkeit :math:`\omega_2` beschleunigt, so
muss in Gleichung :eq:`eqn-rotationsarbeit` anstelle :math:`\omega` die
Differenz :math:`\Delta \omega = \omega_2 - \omega_1` beider
Winkelgeschwindigkeiten eingesetzt werden.

.. Rotationsarbeit \Delta W_{\mathrm{rot}} = M \cdot \Delta \varphi = J \cdot \alpha \cdot \Delta \varphi
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
      \Rightarrow F_1 \cdot s_1 = \frac{1}{2} \cdot F_2 &\, \cdot \, 2 \cdot s_2
      = F_2 \cdot s_2

* Um einen Körper mit einer Gewichtskraft :math:`F_{\mathrm{G}}` auf eine Höhe
  :math:`h` zu heben, ist die Hubarbeit :math:`W_{\mathrm{Hub}} = F_{\mathrm{G}} \cdot
  h` nötig. Verschiebt man ihn hingegen entlang des längeren Weges :math:`l`
  einer :ref:`schiefen Ebene <Schiefe Ebene>` nach oben, so ist die nötige
  Kraft :math:`F` um das Verhältnis :math:`\frac{h}{l}` geringer. Es gilt:

  .. math::

      F \cdot l = F_{\mathrm{G}} \cdot h


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die Arbeits-Formel :math:`W = F \cdot s` gilt streng genommen nur, wenn
    die wirkende Kraft F konstant ist. Ist die Kraft nur innerhalb einzelner
    Zeitabschnitte konstant, so muss man die Formel für jeden dieser
    Zeitabschnitte einzeln anwenden und die jeweiligen Teilbeträge summieren.

    .. math::

        W = \sum_{i}^{} F_{\mathrm{i}} \cdot s_{\mathrm{i}}

    Im Fall einer sich kontinuierlich ändernden Kraft wird aus der Summe
    :math:`(\sum_{}^{})` ein Integral :math:`(\int_{}^{})`.

.. [#]  Um die Formel für die Beschleunigungsarbeit :math:`W_{\mathrm{B}}`
    herzuleiten, geht man von der allgemeinen Definition der Arbeit :math:`W = F
    \cdot s` aus. Für die Kraft :math:`F` kann man das allgemeine Kraftgesetz
    :math:`F = m \cdot a` einsetzen. Für die Wegstrecke kann man die
    :ref:`Bremsformel <Bremsformel>` :math:`v^2-v_0^2 = 2 \cdot a \cdot s` nach
    :math:`s` auflösen. Erfolgt die Beschleunigung aus dem Stillstand
    :math:`(v_0=0)`, so ist :math:`s = \frac{v^2}{2 \cdot a}`. Setzt man
    auch diesen Ausdruck in die allgemeine Definition der Arbeit ein, so erhält
    man:

    .. math::

        W_{\mathrm{B}} = F \cdot s =  (m \cdot a)  \cdot \frac{v^2}{2 \cdot a} =
        \frac{1}{2} \cdot m \cdot v^2

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Experimente <Experimente Mechanische Arbeit>` und
    :ref:`Übungsaufgaben <Aufgaben Mechanische Arbeit>`.


