
.. index:: Allgemeine Gasgleichung, Allgemeine Gaskonstante
.. _Allgemeine Gasgleichung:

Die allgemeine Gasgleichung
===========================

Die :ref:`Zustandsgleichung für ideale Gase <Zustandsgleichung eines idealen
Gases>` in einem geschlossenen System kann auch in folgender Form geschrieben
werden:

.. math::

    p \cdot V = \text{konst.} \cdot T

Betrachtet man :math:`\unit[1]{mol}` eines Gases, so ist der konstante Faktor
auf der rechten Seite der obigen Gleichung gleich der allgemeinen Gaskonstante
:math:`R = \unit[8,31]{\frac{J}{mol \cdot K}}`; betrachtet man
:math:`\unit[n]{mol}` an Teilchen, so ist die Konstante entsprechend
:math:`n`-mal so groß. Es gilt somit für beliebige Gasmengen innerhalb eines
geschlossenen Systems:

.. math::
    :label: eqn-allgemeine-gasgleichung

    p \cdot V = n \cdot R \cdot T

Diese Gleichung wird als "allgemeine Gasgleichung" bezeichnet und gilt in sehr
guter Näherung bei nicht allzu hohen Drücken auch für reale Gase.

.. index:: Normalbedingungen, Normalvolumen
.. _Normalvolumen:
.. _Normalvolumen eines Gases:

.. rubric:: Normalvolumen eines Gases:

Mit der Gleichung :eq:`eqn-allgemeine-gasgleichung` kann beispielsweise bestimmt
werden, welches Volumen :math:`V_0` die Stoffmenge :math:`n=\unit[1]{mol}` eines
idealen Gases unter Normalbedingungen, also bei einem Druck von
:math:`p=\unit[101,3]{kPa}` und einer Temperatur von :math:`T=\unit[273,15]{K}`
einnimmt:

.. math::

    V_0 = \frac{\unit[1]{mol} \cdot \unit[8,31]{\frac{J}{mol \cdot K}} \cdot
    \unit[273]{K}}{\unit[101,3 \cdot 10^3]{Pa}} \approx \unit[0,0224]{\frac{N
    \cdot m}{\frac{N}{m^2}}} = \unit[0,0224]{m^3} = \unit[22,4]{l}

Bei der obigen Rechnung wurde die Einheit Joule als Newton mal Meter und die
Einheit Pascal als Newton je Quadratmeter geschrieben. Als Ergebnis erhält man
fest, dass ein Mol eines idealen Gases (und in guter Näherung auch ein Mol
eines realen Gases) unter Normalbedingungen ein Volumen von rund
:math:`\unit[22,4]{Litern}` einnimmt.

.. index:: Stoffmenge, Avogadro-Konstante
.. _Teilchenzahl und molare Masse:

.. rubric:: Teilchenzahl und molare Masse

Die allgemeine Gasgleichung stellt nicht nur einen Zusammenhang zwischen den
drei Zustandsgrößen Druck, Volumen und Temperatur her, sondern gibt
zusätzlich auch noch eine Beziehung zur Teilchenanzahl an. Da eine Stoffmenge
von :math:`n=\unit[1]{mol}` einer Anzahl von :math:`N_{\mathrm{A}} =
\unit[6,022\cdot 10^{23}]{Teilchen}` entspricht ("Avogadro-Konstante"), folgt
als weiterer Zusammenhang zwischen Stoffmenge :math:`n` und Teilchenzahl
:math:`N`:

.. math::
    :label: eqn-stoffmenge-und-teilchenzahl

    n = \frac{N}{N_{\mathrm{A}}}

.. index:: Molare Masse

In einer Stoffmenge von :math:`\unit[n]{mol}` eines Gases sind also :math:`n
\cdot N_{\mathrm{A}}` Teilchen enthalten. Die Stoffmenge :math:`n` lässt sich
wiederum bestimmen, wenn man die Masse :math:`m` eines Gases und seine molare
Masse :math:`m_{\mathrm{Mol}}` kennt:

.. math::

    n = \frac{m}{m_{\mathrm{M}}}

Die molare Masse :math:`m_{\mathrm{M}}` eines Gases kann anhand der relativen
Atommasse :math:`u` eines Elements aus einem :ref:`Periodensystem der Elemente
<Periodensystem der Elemente>` abgelesen werden. Bei Edelgasen, deren
Teilchen aus einzelnen Atomen bestehen, ist die molare Masse mit der relativen
Atommasse identisch. Bei Gasen wie Sauerstoff :math:`(\ce{O2})` oder Stickstoff
:math:`(\ce{N2})`, deren Teilchen aus zwei-atomigen Molekülen bestehen,
entspricht die molare Masse der doppelten relativen Atommasse des Elements.

*Beispiele:*

* Wie groß ist die molare Masse :math:`m_{\mathrm{M}}` von Helium
  :math:`(\ce{He})`, Stickstoff :math:`(\ce{N2})`, Sauerstoff :math:`(\ce{O2})`
  und Argon :math:`(\ce{Ar})`?

  Helium hat eine relative Atommasse von :math:`\unit[4]{\frac{g}{mol}}`. Da
  Helium-Atome als einzelne Atome in Heliumgas auftreten, gilt auch für die
  molare Masse von Helium:

  .. math::

      m_{\mathrm{M,Helium}} = \unit[4]{\frac{g}{mol}}

  Stickstoff hat eine relative Atommasse von  :math:`\unit[14]{\frac{g}{mol}}`,
  Sauerstoff eine relative Atommasse von :math:`\unit[16]{\frac{g}{mol}}`.
  Sowohl Stickstoff wie auch Sauerstoff treten als zweiatomige Moleküle auf.
  Die molare Masse dieser Gase ist somit doppelt so gross wie die relative
  Atommasse der Elemente:

  .. math::

      m_{\mathrm{M,Stickstoff}} &= 2 \cdot \unit[14]{\frac{g}{mol}}=
      \unit[28]{\frac{g}{mol}} \\
      m_{\mathrm{M,Sauerstoff}} &= 2 \cdot \unit[16]{\frac{g}{mol}}=
      \unit[32]{\frac{g}{mol}} \\

  Argon hat eine relative Atommasse von :math:`\unit[40]{\frac{g}{mol}}`. Da
  Argon ebenso wie Helium als ein-atomiges Gas auftritt, gilt für die molare
  Masse von Argon:

  .. math::

      m_{\mathrm{M,Argon}} = \unit[40]{\frac{g}{mol}}

* Wie groß ist die molare Masse von Luft?

  Luft besteht näherungsweise aus :math:`78\%` Stickstoff, :math:`21\%`
  Sauerstoff und :math:`1\%` Argon. Die molare Masse von Luft entspricht der
  durchschnittlichen molaren Masse ihrer Bestandteile, wobei die
  unterschiedlichen Mengenverhältnisse als Gewichtungsfaktoren berücksichtigt
  werden:

  .. math::

      m_{\mathrm{M, Luft}} = 0,78 \cdot \unit[28]{\frac{g}{mol}} + 0,21 \cdot
      \unit[32]{\frac{g}{mol}} + 0,01 \cdot \unit[40]{\frac{g}{mol}} \approx
      \unit[29]{\frac{g}{mol}}

Anhand der molaren Masse eines Gases kann mittels der allgemeinen Gasgleichung
beispielsweise dessen Dichte bei einem bestimmten Druck und einer bestimmten
Temperatur bestimmt werden:

.. math::

    p \cdot V = \frac{m}{m_{\mathrm{M}}} \cdot R \cdot T \quad \Leftrightarrow
    \quad \rho = \frac{m}{V} = \frac{p \cdot m_{\mathrm{M}}}{R \cdot T}

Für Luft gilt beispielsweise unter Normalbedingungen, also bei :math:`p =
\unit[101,3]{kPa}` und :math:`T = \unit[273]{K}`:

.. math::

    \rho_{\mathrm{Luft}} = \frac{\unit[101,3 \cdot 10^3]{Pa} \cdot
    \unit[29]{\frac{g}{mol}}}{\unit[8,31]{\frac{J}{mol \cdot K}} \cdot
    \unit[273]{K}} \approx \unit[1294,9]{\frac{\frac{N}{m^2} \cdot g}{N \cdot
    m}} = \unit[1294,9]{\frac{ g}{m^3}} \approx \unit[1,29]{\frac{kg}{m^3}}

Hierbei wurde für die Einheit Pascal durch Newton je Quadratmeter und die
Einheit Joule durch Newton mal Meter ersetzt. Der so berechnete Dichte-Wert von
Luft stimmt mit experimentellen Messungen sehr gut überein.

.. index:: Partialdruck
.. _Gasgemische:
.. _Partialdruck:
.. _Gasgemische und Partialdrücke:

Gasgemische und Partialdrücke
-----------------------------

Bei Gasgemischen, wie beispielsweise Luft, kann die allgemeine Gasgleichung für
jede einzelne Komponente aufgeschrieben werden:

.. math::

    p_{\mathrm{i}} \cdot V = n_{\mathrm{i}} \cdot R \cdot T

In dieser Gleichung gibt :math:`n_{\mathrm{i}}` die Stoffmenge der :math:`i`-ten
Komponente an. Die zu Grunde liegende Idee hierbei ist wiederum, dass sich die
Gasteilchen nicht gegenseitig beeinflussen, die gleiche Temperatur haben sowie
das gleiche Volumen einnehmen. Man kann die obige Gleichung auch so deuten, dass
jede der :math:`i` Komponenten zu einem eigenen "Partialdruck"
:math:`p_{\mathrm{i}}` führt:

.. math::

    p_{\mathrm{i}} = \frac{n_{\mathrm{i}} \cdot R \cdot T}{V}

Der Gesamtdruck eines Gasgemisches ist dann die Summe aller Partialdrücke der
einzelnen Komponenten. Dieses Prinzip wird nach ihrem Entdecker auch als Gesetz
von `Dalton <https://de.wikipedia.org/wiki/John_Dalton>`_ bezeichnet:

.. math::

    p_{\mathrm{ges}} = \sum_{i=1}^{n} p_{\mathrm{i}} = p_1 + p_2 + \ldots

Luft besteht beispielsweise zu :math:`78\%` aus Stickstoff :math:`(\ce{N2})`, zu
:math:`20,95\%` aus Sauerstoff :math:`(\ce{O2})` und zu :math:`0,5\%` aus
anderen Gasen (z.B. Argon und Kohlenstoffdioxid). Die Partialdrücke der
einzelnen Gase entsprechen den Mol-Anteilen :math:`\frac{n_{\mathrm{i}}}{n}` der
einzelnen Substanzen. Bei einem Normal-Luftdruck von :math:`\unit[1,01]{bar}`
ergibt sich folglich ein Partialdruck von :math:`\unit[0,78]{bar}` für
Stickstoff, ein Partialdruck von :math:`\unit[0,2095]{bar}` für Sauerstoff usw.

Luft kann zudem Wasserdampf aufnehmen, die dem Sättigungs-Dampfdruck von Wasser
entspricht -- dieser ist temperaturabhängig und beträgt bei
:math:`\unit[20]{\degree}` etwa :math:`\unit[0,023]{bar}`.

.. Partialdruck entspricht Molanteil \frac{n_{\mathrm{i}}}{n}!

.. index:: Van-der-Waals-Gleichung
.. _Van-der-Waals-Gleichung:

Die Van-der-Waals-Gleichung
---------------------------

Die allgemeine Gasgleichung :eq:`eqn-allgemeine-gasgleichung` gilt in guter
Näherung nur für Gase mit geringer Dichte. Bei großen Gasdichten, beispielsweise
bei gesättigtem Dampf, können reale Gase nicht mehr als "ideale" Gase betrachtet
werden. In diesem Fall muss einerseits die Wechselwirkung zwischen den
Gasmolekülen, andererseits auch das Eigenvolumen der Gasteilchen berücksichtigt
werden. Aus der allgemeinen Gasgleichung ergibt sich mit den entsprechenden
Korrektur-Termen die so genannte Van-der-Waals-Gleichung, die für :math:`n` Mole
eines Gases folgendermaßen lautet:

.. math::

    \left( p + \frac{a}{V^2} \right) \cdot \left( V  - b\right) = n \cdot R \cdot T

Hierbei bezeichnet :math:`b` das Eigenvolumen der Gasteilchen; durch den
Korrekturterm :math:`\frac{a}{V^2}` wird der durch die Wechselwirkungen der
Gasteilchen verursachte Binnendruck berücksichtigt.

In einem :math:`p(V)`-Diagramm verlaufen die Isothermen oberhalb einer
bestimmten, als "kritisch" bezeichneten Temperatur :math:`T_{\mathrm{kr}}`
ebenso wie die Isothermen von idealen Gasen.  Unterhalb von
:math:`T_{\mathrm{kr}}` sind die Isothermen S-förmig gebogen.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Allgemeine
    Gasgleichung>`.

