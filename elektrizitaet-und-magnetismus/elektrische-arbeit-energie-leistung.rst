.. _Elektrische Arbeit, Energie und Leistung:

Elektrische Arbeit, Energie und Leistung
========================================

.. index::
    single: Energieformen; Elektrische Energie

.. _Generator:
.. _Stromgenerator:
.. _Elektrische Arbeit und Energie:

Elektrische Arbeit und Energie
------------------------------

Zur Bereitstellung einer bestimmten Menge an elektrischer Energie muss durch
einen Stromgenerator ein entsprechender Betrag an Arbeit aufgewendet werden.
[#G1]_

Zur Herleitung einer Formel für die elektrische Arbeit :math:`W_{\mathrm{el}}`
kann man die Definitionen der elektrischen Spannung :math:`U` und der
elektrischen Stromstärke :math:`I` miteinander kombinieren. Aus der Definition
der elektrischen Spannung folgt:

.. math::
    :label: eqn-spannung-definition

    U = \frac{W}{Q} \quad \Leftrightarrow \quad W = U \cdot Q


Die Ladung :math:`Q` kann wiederum mit Hilfe der Definition der Stromstärke
folgendermaßen beschrieben werden:

.. math::
    :label: eqn-stromstärke-definition

    I = \frac{Q}{t} \quad \Leftrightarrow \quad Q = I \cdot t

Insgesamt ergibt die Kombination dieser beiden Gleichungen folgende Formel für
die elektrische Arbeit:

*Definition:*

    Die elektrische Arbeit, die ein Stromgenerator verrichtet, ist proportional
    zur Spannung :math:`U` und zur Stromstärke :math:`I` des bereitgestellten
    Stroms sowie zur Zeitdauer :math:`t`, über die sich der Stromfluss
    erstreckt.

.. math::
    :label: eqn-elektrische-arbeit

    W_{\mathrm{el}} = U \cdot I \cdot t

Die aufgebrachte elektrische Arbeit kann entweder direkt genutzt oder als
elektrische Energie :math:`E_{\mathrm{el}}` in Kondensatoren und Akkumulatoren
gespeichert werden :math:`(E_{\mathrm{el}} = W_{\mathrm{el}})`. [#E1]_

*Einheit:*

    Die elektrische Arbeit sowie die elektrische Energie wird in Joule
    :math:`(\unit[1]{J} = \unit[1]{W \cdot s})` oder gebräuchlicher in
    Wattstunden :math:`(\unit{Wh})` bzw. Kilowattstunden
    :math:`(\unit{kWh})` angegeben. Dabei gelten folgende Zusammenhänge:

.. math::

    \unit[1]{J} &= \unit[1]{W \cdot s} = \unit[1]{V} \cdot \unit[1]{A} \cdot
    \unit[1]{s} \\
    \unit[1]{Wh} &= \unit[60 \cdot 60]{W \cdot s} = \unit[3\,600]{Ws}

.. math::

    \unit[1]{kWh} &= \unit[1\,000]{Wh}


.. _Elektrische Leistung:

Elektrische Leistung
--------------------

Die elektrische Leistung :math:`P_{\mathrm{el}}`, die ein Stromgenerator
aufbringt oder ein Verbraucher benötigt, ist gleich der je Zeit :math:`\Delta t`
verrichteten elektrischen Arbeit :math:`\Delta W_{\mathrm{el}}`:

.. math::

    P_{\mathrm{el}} = \frac{\Delta W_{\mathrm{el}}}{\Delta t} = \frac{U \cdot I
    \cdot \Delta t}{\Delta t} = U \cdot I

Damit lässt sich die elektrische Leistung folgendermaßen definieren:

*Definition:*

    Die elektrische Leistung :math:`P_{\mathrm{el}}`, die von einem elektronischen
    Bauteil oder Stromkreis umgesetzt wird, ist proportional zu der am Bauteil
    anliegenden Spannung :math:`U` sowie der durch das Bauteil fließenden
    Stromstärke :math:`I`.

.. math::
    :label: eqn-elektrische-leistung

    P _{\mathrm{el}} = U \cdot I

*Einheit:*

    Ebenso wie die mechanische Leistung wird die elektrische Leistung in der
    Einheit Watt :math:`(\unit{W})` angegeben. Dabei gilt: [#L1]_

.. math::

    \unit[1]{W} = \unit[1]{V} \cdot \unit[1]{A}

Auf fast allen Elektro-Geräten findet sich neben der Angabe der zulässigen
Betriebsspannung auch eine Angabe einer damit verbundenen elektrischen
Stromstärke oder Leistung. [#L2]_ Zu beachten ist dabei, dass diese Werte nur
bei der angegebenen Spannung gelten; da eine höhere Spannung in der Regel auch
eine höhere Stromstärke zur Folge hat, nimmt die Leistung mit zunehmender
Spannung überproportional zu.


.. _Belastbarkeit von elektrischen Bauteilen:
.. _Wärmeentwicklung in elektrischen Bauteilen:
.. _Exkurs Belastbarkeit von elektrischen Bauteilen:
.. _Exkurs Wärmeentwicklung in elektrischen Bauteilen:

.. rubric:: Exkurs: Wärmeentwicklung in elektrischen Bauteilen

Mittels des Ohmschen Gesetzes :math:`U = R \cdot I` kann der obige Zusammenhang
:math:`P_{\mathrm{el}} = U \cdot I` zwischen der elektrischen Leistung
:math:`P_{\mathrm{el}}` sowie der Spannung :math:`U` und der Stromstärke
:math:`I` auch folgendermaßen ausgedrückt werden:

* Setzt man für die Stromstärke :math:`I = \frac{U}{R}` in die
  Leistungs-Gleichung :eq:`eqn-elektrische-leistung` ein, so erhält man:

  .. math::
      :label: eqn-leistung-spannungsabhaengig

      P = U \cdot I = U \cdot \frac{U}{R} = \frac{U^2}{R}

* Setzt man für die Spannung :math:`U = R \cdot I` in die Leistungs-Gleichung
  :eq:`eqn-elektrische-leistung` ein, so erhält man:

  .. math::
      :label: eqn-leistung-stromabhaengig

      P = U \cdot I = (R \cdot I) \cdot I = R \cdot I^2

Bei beiden Darstellungen erkennt man, dass die elektrische (Heiz-)Leistung bei
konstant bleibendem Widerstand quadratisch mit einer zunehmenden Spannung
beziehungsweise Stromstärke ansteigt.

*Beispiel:*

* Auf einem regelbaren Demo-Widerstand ist ein maximaler Widerstandswert von
  :math:`R_{\mathrm{max}} = \unit[50]{\Omega}` angegeben und eine maximale
  Belastbarkeit von :math:`P_{\mathrm{max}} = \unit[0,5]{W}`.

  - Wie groß darf die am Widerstand anliegende Spannung :math:`U_{\mathrm{max}}`
    eines regelbaren Netzgerätes maximal sein, wenn kein zusätzliches Bauteil im
    Stromkreis eingebaut ist?

  - Auf welchen Wert :math:`U` muss die Spannung gesenkt werden, wenn der
    Widerstand auf :math:`R = \unit[25]{\Omega}` eingestellt ist?

  Die jeweils maximal mögliche Spannung kann bei einem gegebenen Widerstand
  und einer gegebenen maximalen Leistung berechnet werden, indem man die Formel
  :eq:`eqn-leistung-spannungsabhaengig` nach :math:`U` auflöst. Man erhält für
  :math:`P_{\mathrm{max}} = \unit[0,5]{W}` und :math:`R=\unit[50]{\Omega}`:

  .. math::

      P_{\mathrm{max}} = \frac{U_{\mathrm{max}}^2 }{R_{\mathrm{max}}} \quad
      \Longleftrightarrow \quad U_{\mathrm{max}} = \sqrt{P_{\mathrm{max}} \cdot
      R_{\mathrm{max}}} \\ U_{\mathrm{max}} = \sqrt{\unit[0,5]{W} \cdot
      \unit[50]{\Omega}} = \unit[5,0]{V}

  Die Einheit ergibt sich aus :math:`\unit{W} = \unit{V \cdot A}` und
  :math:`\unit{\Omega} = \unit{\frac{V}{A}}`; als Produkt ergibt also die
  Einheit :math:`\unit{W \cdot \Omega} = \unit{V^2}`.

  Reduziert man den Widerstand auf :math:`R=\unit[25]{\Omega}`, so darf bei
  einer gleichen maximalen Belastbarkeit nur folgende Spannung :math:`U` angelegt werden:

  .. math::

      U = \sqrt{P_{\mathrm{max}} \cdot R} = \sqrt{\unit[0,5]{W} \cdot
      \unit[25]{\Omega}} \approx \unit[3,54]{V}

  Bei einem geringeren Widerstandswert muss also auch die Spannung geringer
  gewählt werden, um das Bauteil nicht zu überlasten.

.. todo Leistungshyperbel?

.. _Stromerzeugung und Stromverbrauch:

Stromerzeugung und Stromverbrauch
---------------------------------

In jedem Stromkreis muss die Menge der bereitgestellten Energie -- da die
Gesamtenergie stets erhalten bleibt und elektrische Ladung weder erzeugt noch
vernichtet, sondern nur übertragen werden kann -- stets der Menge an
verbrauchter elektrischer Energie entsprechen. [#E2]_

In einem so großen Stromnetz wie dem der Bundesrepublik Deutschland gibt es
selbstverständlich mehr als einen Stromgenerator; insgesamt gesehen muss der
Kraftwerkspark allerdings die Verbraucherlast tragen sowie die sich beim
Stromtransport ergebenden Leitungsverluste ausgleichen. Bei einer möglichst
optimalen Zusammenstellung der Gesamtleistung mittels der verschiedenen
Kraftwerkstypen sind ökologische, ökonomische sowie technische Aspekte
gleichermaßen von Bedeutung.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#G1] Spannung erzeugende Geräte, die zur Energie-Gewinnung Treibstoffe
    verbrennen, haben meist einen Verbrennungsmotor oder eine Gas-Turbine als
    Antrieb; der eigentliche Generator wandelt dann die mechanische Energie in
    elektrische Energie um.

    Im verallgemeinerten Sinn bezeichnet man sämtliche Spannung erzeugende Geräte
    als Generatoren, also beispielsweise auch Solarzellen oder Thermo-Elemente.

.. [#E1] Streng genommen speichern Akkumulatoren die zugeführte elektrische
    Energie in Form von chemischer Energie. Beide Energieformen lassen sich
    allerdings (bis auf geringe Wärmeverluste) vollständig ineinander
    umwandeln -- ein voll geladener Akkumulator stellt bei seiner Nutzung
    wiederum elektrische Energie bereit.

.. [#L1] Für größere Leistungsangaben ist auch die Einheit Kilowatt
    :math:`(\unit[]{kW})` gebräuchlich. Dabei gilt: :math:`\unit[1]{kW} =
    \unit[1\,000]{W}`

.. [#L2] Die jeweils fehlende Angabe kann durch die beiden bekannten Größen
    mittels Gleichung :eq:`eqn-elektrische-leistung` bestimmt werden.

.. [#E2] Auch in Speicheranlagen wie Pumpspeicherkraftwerken oder Akkumulatoren
    wird zunächst elektrische Energie verbraucht, z.B. um eine große Menge
    Wasser auf eine bestimmte Höhe zu pumpen oder bestimmte chemische
    Reaktionen zu ermöglichen; umgekehrt können derartige Anlagen bei
    Bedarf die gespeicherte Energiemenge mit nur geringen (Wärme-)Verlusten
    wieder als elektrische Energie bereitstellen.

.. only:: html

    .. rubric:: Download:

    Hier kann die Handreichung zum Vortrag :download:`Ökologisch sinnvolle
    Stromerzeugung (2011, PDF, 10 Seiten)
    <oekologisch-sinnvolle-stromerzeugung.pdf>` heruntergeladen werden.

.. raw:: html

    <hr />

.. hint::

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben Elektrische
    Arbeit, Energie und Leistung>`.

