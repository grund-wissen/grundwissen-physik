.. _Elektrische Arbeit, Energie und Leistung:

Elektrische Arbeit, Energie und Leistung
========================================

.. index:: 
    single: Energieformen; Elektrische Energie

.. _Elektrische Arbeit und Energie:

Elektrische Arbeit und Energie
------------------------------

Zur Bereitstellung einer bestimmten Menge an elektrischer Energie muss durch
einen Stromgenerator ein entsprechender Betrag an Arbeit aufgewendet werden. 

Zur Herleitung einer Formel für die elektrische Arbeit :math:`W _{\rm{el}}` kann
man die Definitionen der elektrischen Spannung :math:`U` und der elektrischen
Stromstärke :math:`I` miteinander kombinieren. Aus der Definition der
elektrischen Spannung folgt:

.. math::
    
    U = \frac{W}{Q} \quad \Leftrightarrow \quad W = U \cdot Q

..  :label: eqn-definition-spannung

Die Ladung :math:`Q` kann wiederum mit Hilfe der Definition der Stromstärke
folgendermaßen beschrieben werden:

.. math::
    
    I = \frac{Q}{t} \quad \Leftrightarrow \quad Q = I \cdot t

..  :label: eqn-definition-stromstärke

Insgesamt ergibt die Kombination dieser beiden Gleichungen folgende Formel für
die elektrische Arbeit:

*Definition:*

    Die elektrische Arbeit, die ein Stromgenerator verrichtet, ist proportional
    zur Spannung :math:`U` und zur Stromstärke :math:`I` des bereitgestellten
    Stroms sowie zur Zeitdauer :math:`t`, über die sich der Stromfluss
    erstreckt.

.. math::
    :label: eqn-elektrische-arbeit
    
    W _{\rm{el}} = U \cdot I \cdot t

Die aufgebrachte elektrische Arbeit kann entweder direkt genutzt oder als
elektrische Energie :math:`E _{\rm{el}}` in Kondensatoren und Akkumulatoren
gespeichert werden :math:`(E _{\rm{el}} = W _{\rm{el}})`. [#E1]_

*Einheit:*

    Die elektrische Arbeit sowie die elektrische Energie wird in Joule
    :math:`(\unit[1]{J} = \unit[1]{W \cdot s})` oder gebräuchlicher in
    Wattstunden :math:`(\unit[]{Wh})` bzw. Kilowattstunden
    :math:`(\unit[]{kWh})` angegeben. Dabei gelten folgende Zusammenhänge:

.. math::
    
    \unit[1]{J} &= \unit[1]{W \cdot s} = \unit[1]{V} \cdot \unit[1]{A} \cdot \unit[1]{s} \\
    \unit[1]{Wh} &= \unit[60 \cdot 60]{W \cdot s} = \unit[3\,600]{Ws} 

.. math::
    
    \unit[1]{kWh} &= \unit[1\,000]{Wh}
    

.. _Elektrische Leistung:

Elektrische Leistung
--------------------

Die elektrische Leistung, die ein Stromgenerator aufbringt oder ein Verbraucher
benötigt, ist gleich der je Zeit verrichteten elektrischen Arbeit:

.. math::
    
    P _{\rm{el}} = \frac{W _{\rm{el}}}{t} = \frac{U \cdot I \cdot t}{t} = U
    \cdot I

Damit lässt sich die elektrische Leistung folgendermaßen definieren:

*Definition:*

    Die elektrische Leistung :math:`P _{\rm{el}}`, die von einem elektronischen
    Bauteil oder Stromkreis umgesetzt wird, ist proportional zu der am Bauteil
    anliegenden Spannung :math:`U` sowie der durch das Bauteil fließenden
    Stromstärke :math:`I`.

.. math::
    :label: eqn-elektrische-leistung
    
    P _{\rm{el}} = U \cdot I


*Einheit:*

    Ebenso wie die mechanische Leistung wird die elektrische Leistung in der
    Einheit Watt :math:`(\unit[]{W})` angegeben. Dabei gilt: [#L1]_

.. math::
    
    \unit[1]{W} = \unit[1]{A} \cdot \unit[1]{s}

Auf fast allen Elektro-Geräten findet sich neben der Angabe der zulässigen
Betriebsspannung auch eine Angabe einer damit verbundenen elektrischen
Stromstärke oder Leistung. [#L2]_ Zu beachten ist dabei, dass diese Werte nur
bei der angegebenen Spannung gelten; da eine höhere Spannung in der Regel auch
eine höhere Stromstärke zur Folge hat, nimmt die Leistung mit zunehmender
Spannung überproportional zu.


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

    Zu diesem Abschnitt gibt es :ref:`Übungsaufgaben <Aufgaben zu elektrischer
    Arbeit, Energie und Leistung>`.

