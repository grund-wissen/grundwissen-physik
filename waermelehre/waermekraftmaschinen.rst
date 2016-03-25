.. _Wärmekraftmaschinen:

Wärmekraftmaschinen
===================

Wärmekrafmaschinen wandeln chemische Energie durch Verbrennung in thermische
Energie um. 

.. Über einen Kurbel-Antrieb wird die Hubkraft in eine Drehbewegung überführt und
.. ist damit für die Antriebsräder nutzbar. 


.. _Carnot-Prozess:

Der Carnot-Prozess
------------------

.. Der Carnot-Prozess beschreibt den Idealfall einer Wärmekraftmaschine, liefert
.. also bei gegebenen Temperaturniveaus den bestmöglichen Wirkungsgrad
.. :math:`\eta`; Es gibt allerdings keine technische Realisierung dieses Prozesses.

.. Der Kreisprozess läuft von den Punkten 1 bis 4 durch die Stufen der adiabaten
.. Verdichtung, isothermen Verbrennung, adiabaten Expansion, isotherme Verdichtung.

.. * 1-2 Bei der adiabaten Verdichtung findet kein Wärmeaustausch mit der Umgebung
..   statt. Da aber mechanische Arbeit entgegen des Druckes verrichtet wird,
..   entsteht Wärme, wobei wegen des geschlossenen Systems die Entropie konstant
..   bleibt.
.. * 2-3 Bei der isothermen Verbrennung geht man davon aus, dass bei konstanter
..   Tempera- tur der Brennstoff verbrannt wird. Es wird Energie zugeführt. Das
..   heisst im T-s-Diagramm muss die Entropie zunehmen bei konstanter Temperatur.
.. * 3-4 Bei der adiabaten Expansion wird expandiert, ohne Wärme an die Umgebung
..   abzuge- ben. Das heisst wir müssen mechanische Arbeit verrichten, die an den
..   Kurbeltrieb rotatorisch übergeben wird. Das ist die thermische
..   Energiedifferenz zwischen der zugeführten und der abgeführten Wärmeenergie.
.. * 4-1 Bei der isothermen Verdichtung ist die Temperatur wieder konstant wobei
..   gleichzeitig Wärme abgeführt wird, um sie konstant zu halten.

.. Zwischen Punkt 4 und 1 wird Wärme abgeführt nachdem die mechanische Arbeit schon
.. verrichtet worden ist. Das heisst unsere Nutzwärme ist die Differenz der
.. zugeführten Wärme von der abgeführten Wärme. Es ergibt sich der thermische
.. Wirkungsgrad unseres Carnot-Prozesses zu:

.. .. math::

..     \eta _{\mathrm{th}} = \frac{Q _{\mathrm{nutz}}}{Q _{\mathrm{zu}}} =
..     \frac{Q_{23} - Q_{41}}{Q_{23}} = \frac{T _{\mathrm{max}}-
..     T_{\mathrm{min}}}{T_{\mathrm{max}}}

.. Dabei ist :math:`T_{\mathrm{min}}` die Temperatur, bei der die Wärme abgeführt
.. wird und :math:`T_{\mathrm{max}}` die Temperatur nach der Zündung, bei der die
.. Wärme also zugeführt wird. :math:`Q_{23}` ist die Energie, die in Form von Wärme
.. während der Temperatur :math:`T_{\mathrm{max}}` zugeführt wird (es wird isotherm
.. verbrannt) und :math:`Q_{41}` ist die Wärmemenge, die bei der Temperatur
.. :math:`T_{\mathrm{min}}` abgeführt wird (es wird isotherm verdichtet als Teil
.. des Ladungswechsels).

.. Die benötigte Verdichtearbeit ist die Arbeit, die aufgebracht werden muss, um
.. das Volumen zu verdichten. Die abgegebene Expansionsarbeit ist die Fläche unter
.. der Expansionskurve.

.. An dem T-s-Diagramm können wir ablesen, dass es für einen großen Wirkungsgrad
.. günstig ist, wenn bei hoher Temperatur T max die Wärmezufuhr Q 23 stattfindet.
.. Das erreicht man beim Verbrennungsmotor durch eine große Verdichtung. Es kann
.. aber auch T min nicht beliebig tief liegen, nämlich maximal bei
.. Umgebungstemperatur. Das ist der Grund, warum der Carnot-Prozess auch keinen
.. Wirkungsgrad von 1 haben kann. 

.. Ideal: Seiliger-Prozess

.. Wegen der schlechten Realisierbarkeit des Carnot-Prozesses nutzt man zur
.. quantiativen Beurteilung des thermodynamischen Prozesses einen anderen
.. Vergleichsprozess: den Seiliger-Prozess. Dieser motorische Kreisprozess
.. beschreibt die Energieumwandlung, wobei die einzelnen Zustandsänderungen des
.. Arbeitsmittles dem tatsächlichen Geschehen im Verbrennungsmotor möglichst nahe
.. kommen sollen. Verbrennungsmotoren werden dabei als geschlossene Systeme
.. angesehen, in denen die Energieumwandlung diskontinuierlich verläuft. Ein
.. Charakteristikum der Kreisprozesse solcher Motoren ist, dass die
.. Zustandsänderungen in einem Arbeitsraum ablaufen, dessen Größe sich durch die
.. Bewegung des Kurbeltriebs im Laufe des Arbeitsspiels ändert. Die Verbrennung und
.. der Gaswechsel werden durch Wärmezu- und -abfuhr ersetzt. Es ist:

.. adiabat \rightarrow s = const.
.. isotherm \rightarrow T = const.
.. isobar -> p = const.
.. isochor -> V = const.

.. Bei dem Seiliger Prozess teilt sich die Verbrennung nach der adiabaten
.. Verdichtung(1-2) in einen Gleichraum- und einen Gleichdruckanteil. Bei ersterem
.. bleibt der Kolben im oberen Totpunkt während ein Teil des Brennstoffes
.. schlagartig isochor verbrennt (2-3) und zu einem Druckanstieg führt durch
.. Wärmezufuhr. Es folgt die isobare Verbrennung (3-4), die den Kolben schon ein
.. Stück nach unten drückt während der Rest des Gases verbrennt.

.. Das Volumen wird dabei soweit expandiert, dass der Druck konstant bleibt. Bis
.. zum unteren Totpunkt passiert nun eine adiabate Expansion (4-5), die die
.. Entropie konstant lässt ohne Wärmeabgabe. Die Öffnung des Auslassventils lässt
.. den Druck schlagartig isochor Abfallen (5-1). Das ist der Ladungswechsel, wo das
.. Abgas ausgestoßen, also die Wärme abgeführt wird. Eine Gaswechselschleife fehlt.

.. Wir haben also eine Wärmezufuhr während isochorem und isobarem
.. Verbrennungsprozess (Q 23 respektive Q 34 ). Diese Energie wird dem System durch
.. die Einspritzung der Frischladung zugeführt. Mechanische Leistung für unseren
.. Kraftfahrzeugantrieb wird während der


.. Dokument fahrzeugtechnik12_1.pdf




















..  Wärmeenergie lässt sich nie vollständig in mechanische Energie oder eine
..  andere makroskopische Energieform umwandeln. Es gibt also kein derartiges
..  Perpetuum mobile, das die unter Abkühlung eines Wärmereservoirs Wärme zu 100%
..  in Arbeit umwandelt, ohne an ein zweites Reservoir Wärme abzugeben.

..  Alle realen Wärmekraftmaschinen beruhen auf irreversiblen Kreisprozessen
..  aufgrund von Reibungsverlusten und Wärmeabgabe durch unvollkommene Isolierung.
..  Sie haben deshalb stets einen geringeren Wirkungsgrad :math:`\eta` als der oben
..  genannte Carnotsche Kreisprozess.

..  Die Entropie eines abgeschlossenen Systems wird nie von selbst, d.h. ohne
..  äußere Einwirkungen, kleiner. In einem derartign System verlaufen alle
..  Vorgänge stets so, dass die Entropie :math:`S` konstant bleibt oder zunimmt.
..  Die Wiederherstellung des Ausgangszustandes ist zwar statistisch gesehen
..  prinzipiell möglich, aber völlig unwahrscheinlich und damit praktisch
..  ausgeschlossen.

..  Bei irreversiblen Prozessen nimmt die Entropie zu, bei reversiblen bleibt sie
..  konstant.


.. Ein Wärmeanteil geht als Wirkungsgradverlust verloren, wird zum Heizen des
.. Passagierraumes genutzt oder als Energie über eine Aufladung dem Prozess wieder
.. zugeführt. Heutige Verbrennungsmotoren arbeiten nach dem Otto- oder dem
.. Diesel-Prinzip. Otto-Motoren drehen von 2600 bis zu 7000/min, Diesel-Motoren bis
.. zu 5000/min. Der Wirkungsgrad von Dieselmotoren ist um ca. 20% besser als der
.. von Verbrennungskraftmaschinen nach dem Otto-Verfahren und liefern zehn mal mehr
.. Leistung mit bis zu 36000kW .

..  .. rubric:: Heiz- und Brennwert von Energieträgern

..  Bei jeder Verbrennung entsteht Wärme. Das Verhältnis aus der bei einer
..  Verbrennung freigesetzten Wärmemenge :math:`Q` zur verbrannten Brennstoffmasse
..  :math:`m` wird als Heizwert :math:`H` bezeichnet:

..  .. math::

    ..  H = \frac{Q}{m}

..  Ist der Heizwert eines Brennstoffs bekannt, so kann umgekehrt die bei der
..  Verbrennung freigesetzte Wärmemenge nach der Formel :math:`Q = m \cdot H`
..  berechnet werden.

..  Bei gasförmigen Brennstoffen bezieht sich der spezifische Heizwert
..  :math:`H_{\rm{G}}` auf das Normvolumen :math:`V _{\rm{N}}` eines Gases (Druck :math:`p =
..  \unit[1,013]{bar}`, Temperatur :math:`T = \unit[0]{\degree C}`):

..  .. math::

    ..  H _{\rm{G}} = \frac{Q}{V _{\rm{N}}}

..  Die bei der Verbrennung eines gasförmigen Brennstoffs kann somit als
..  :math:`H_{\rm{G}} = V _{\rm{N}} \cdot H _{\rm{G}}` berechnet werden.


..  Für den Wirkungsgrad \eta jeder realen Wärmekraftmaschine gilt:

..  .. math::

..  \eta < \eta _{\rm{C}} = \frac{T _{\rm{H}} - T _{\rm{N}}}{T _{\rm{H}}}


