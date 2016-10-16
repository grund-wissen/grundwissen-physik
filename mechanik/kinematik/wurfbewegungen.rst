
.. _Wurfbewegungen:

Wurfbewegungen
==============

Im folgenden Abschnitt werden zunächst eindimensionale, später auch
zweidimensionale Wurfbewegungen näher beschrieben. Als Vereinfachung soll dabei
der Luftwiderstand vernachlässigt werden.

Alle Wurfbewegungen haben die Gemeinsamkeit, dass die geworfenen Objekte eine
Beschleungigung von :math:`g=\unitfrac[9,81]{m}{s^2}` ("Erdbeschleunigung")  in
Richtung des Erdmittelpunkts erfahren. Die einzelnen Wurfbewegungen
unterscheiden sich also lediglich hinsichtlich ihrer Startbedingungen.

.. index:: Freier Fall

Freier Fall
-----------

Als "freien Fall" bezeichnet man einen Bewegungsvorgang, bei dem ein Objekt mit
einer Anfangsgeschwindigkeit von :math:`v_0=0` in einer Höhe :math:`h = s_0`
startet und konstant mit der Erdbeschleunigung :math:`g=
\unitfrac[9,81]{m}{s^2}` beschleunigt wird; der Luftwiderstand wird dabei
vernachlässigt.

Durch die konstante Beschleunigung wird das fallende Objekt mit der Zeit
kontinuierlich beschleunigt. Beginnt der Vorgang zur Zeit :math:`t_0=0`, so gilt
für die Geschwindigkeit :math:`v` des Objekts in Abhängigkeit von der Zeit:

.. math::

    v(t) = -g \cdot t

Für die zurückgelegte Wegstrecke :math:`\Delta s` beziehungsweise den Ort
:math:`s` gilt entsprechend mit :math:`v_0 = 0`:

.. math::

    \Delta s &= - \frac{1}{2} \cdot g \cdot t^2 \\[5pt]
    s(t) &= - \frac{1}{2} \cdot g \cdot t^2 + s_0\\

Beim Aufprall auf dem Boden gilt :math:`s(t)=0`; daraus lässt sich die Falldauer
beziehungsweise die Geschwindigkeit :math:`v_{\mathrm{max}}` beim Aufprall
berechnen:

.. math::

    s(t) = 0 \quad \Longleftrightarrow \quad \frac{1}{2} \cdot g \cdot
    t_{\mathrm{max}}^2 = s_0 \\
    t_{\mathrm{max}} = \sqrt{\frac{2 \cdot s_0}{g}}

.. math::

    v_{\mathrm{max}} = -g \cdot t_{\mathrm{max}} = - g \cdot \sqrt{\frac{2 \cdot
    s_0}{g}} = - \sqrt{\frac{2 \cdot s_0 \cdot g^2}{g}} = - \sqrt{2 \cdot s_0
    \cdot g}


.. _Freier Fall:

* Gilt für die konstante Beschleunigung :math:`a < 0`, so ist die (Halb-)Parabel
  nach unten hin geöffnet.

  - Ohne Anfangsgeschwindigkeit :math:`(v_0=0)` findet eine beschleunigte
    Bewegung in negative :math:`s`-Richtung statt.
  - Mit einer Anfangsgeschwindigkeit :math:`v_0 > 0` ergibt sich ein
    kontinuierliches Abbremsen, wobei der Scheitel der Halbparabel den Bremsweg
    angibt:

  .. math::

      s(t) = v_{\mathrm{0}} \cdot t - \frac{1}{2} \cdot a \cdot t^2

  Bleibt nach einem vollständigen Abbremsen -- wie bei einem senkrechten Wurf
  nach oben -- die Beschleunigung :math:`a<0` weiterhin bestehen, so findet
  anschließend eine beschleunigte Bewegung in negativer :math:`s`-Richtung
  statt. Kann der Luftwiderstand vernachlässigt werden, so spricht man bei
  diesem Vorgang von einem "freien Fall" mit
  :math:`|g|=\unit[9,81]{\frac{m}{s^2}}` und :math:`v_0 = 0`.

*Beispiel:*

* Der Schacht eines Brunnens hat eine Tiefe von :math:`h=\unit[-40]{m}`. Wie
  lange dauert es, bis aus der Höhe :math:`h_0 = \unit[0]{m}` fallender ein
  Stein im freien Fall (ohne Luftwiderstand) am Grund des Schachtes ankommt? Wie
  groß ist seine Geschwindigkeit :math:`v` beim Aufprall?

  Die Bewegung des Steins entspricht einem freien Fall mit der Beschleunigung
  :math:`|g|=\unitfrac[9,81]{m}{s^2}` und der Anfangsgeschwindigkeit
  :math:`v_0=0`. Für die vom Stein zurückgelegte Wegstrecke :math:`\Delta s` gilt
  dabei:

  .. math::

      \Delta s = - \frac{1}{2} \cdot g \cdot \Delta t^2

  Der Vorgang endet, wenn eine Strecke von :math:`\Delta s=\unit[-40]{m}`
  durchlaufen wurde (das negative Vorzeichen ergibt sich, wenn eine Bewegung
  nach oben als "positiv" deklariert wird). Für die Fallzeit :math:`\Delta t`
  gilt also:

  .. math::

      \Delta t = \sqrt{\frac{2 \cdot \Delta s}{-g}} = \sqrt{\frac{2 \cdot
      (\unit[-40]{m})}{\unit[-9,81]{\frac{m}{s^2}}}} \approx \unit[2,86]{s}

  In dieser Zeit erreicht der Stein folgende Geschwindigkeit:

  .. math::

      v = -g \cdot t = -\unit[9,81]{\frac{m}{s^2}} \cdot \unit[2,86]{s} \approx
      \unit[-28,0]{\frac{m}{s}}

  Der Stein erreicht beim Aufprall unter Vernachlässigung des Luftwiderstands
  somit eine Geschwindigkeit von rund :math:`\unit[28]{\frac{m}{s}}`; das
  entspricht rund :math:`\unit[100]{\frac{km}{h}}`.

.. _Senkrechter Wurf nach oben:

Senkrechter Wurf nach oben
--------------------------

Wird ein Objekt senkrecht nach oben geworfen, so startet es in der
:math:`z`-Richtung mit einer positiven Anfangsgeschwindigkeit :math:`v_0`;
gleichzeitig wird es durch die Erdbeschleunigung in die entgegengesetzte
Richtung beschleunigt. Beginnt der Vorgang wiederum zur Zeit :math:`t_0=0`, so
gilt für die Geschwindigkeit :math:`v` des Objekts in Abhängigkeit von der
Zeit:

.. math::

    v(t) = -g \cdot t + v_0

Als Annahme soll zunächst gelten, dass das Objekt in einer Höhe von :math:`s_0 =
0` abgeworfen wird. Dann gilt für den Ort :math:`s` in Abhängigkeit von der
Zeit:

.. math::

    s(t) &= - \frac{1}{2} \cdot g \cdot t^2 + v_0 \cdot t\\

Aus den beiden obigen Gleichungen kann man die maximale Steighöhe :math:`s
_{\mathrm{max}}` berechnen. Die zum Erreichen dieser Höhe benötigte Zeit
:math:`t_{\mathrm{max}}` lässt sich anhand der ersten Gleichung bestimmen; an
diesem Punkt ist nämlich die Geschwindigkeit des Objekts gleich Null: 

.. math::

    v_{\mathrm{0}} - g \cdot t_{\mathrm{max}} = 0 \quad \Leftrightarrow \quad
    t_{\mathrm{max}} = \frac{v_0}{g}

Setzt man diesen Term für :math:`t_{\mathrm{max}}` in die zweite Gleichung ein,
so kann man entsprechend die maximale Steighöhe :math:`s_{\mathrm{max}}`
berechnen:

.. math::

    s_{\mathrm{max}} &= v_0 \cdot t_{\mathrm{max}} - \frac{1}{2} \cdot g \cdot
    t_{\mathrm{max}}^2 \\ &= v_{\mathrm{0}} \cdot \frac{v_0}{g} - \frac{1}{2}
    \cdot g \cdot \left( \frac{v_0}{g}\right)^2 \\ 
    &= \frac{\phantom{..} v_0^2 \phantom{.}}{g} - \frac{1}{2} \cdot
    \frac{\phantom{..}v_0^2 \phantom{.}}{g} \\[6pt] 
    &= \frac{v_0^2}{2 \cdot g}

Nach der doppelten Zeit, also :math:`2 \cdot t_{\mathrm{max}}`, kommt das
Objekt wieder auf dem Boden an. Dies kann man beispielsweise überprüfen,
indem man in der Weg-Zeit-Gleichung :math:`s(t) = 0` setzt und die Gleichung
nach :math:`t` auflöst. (Der Luftwiderstand wird dabei vernachlässigt.)

Die Wegstrecke wird beim Herunterfallen in der gleichen Weise durchlaufen wie
beim Hochwerfen, nur zeitlich umgekehrt. Entsprechend ist auch die
Geschwindigkeit des Objekts, sofern kein Luftwiderstand auftritt, vor
Aufprall wieder gleich der ursprünglichen Geschwindigkeit :math:`v_0`.


.. _Senkrechter Wurf nach unten:

Senkrechter Wurf nach unten
---------------------------

Kann ein geworfenes Objekt -- beispielsweise im Anschluss an einen
senkrechten Wurf nach oben -- nach dem Erreichen seiner Ausgangslage weiter
herab fallen, so führt ab diesem diesem Zeitpunkt einen so genannten senkrechten
Wurf nach unten aus; seine Anfangsgeschwindigkeit beträgt dabei :math:`-v_0`.

Für die Geschwindigkeit :math:`v` des Objekts gilt in Abhängigkeit von
der Zeit :math:`t`:

.. math::

    v(t) = - g \cdot t - v_0 

Für den Ort des Objekts gilt im zeitlichen Verlauf entsprechend:

.. math::

    s(t) = -\frac{1}{2} \cdot g \cdot t^2 -v_0 \cdot t + s_{\mathrm{z,0}}

Das Koordinatensystem wurde ursprünglich so festgelegt, dass sich der Nullpunkt
der :math:`z`-Achse in Höhe der Abwurfstelle, also in einer Höhe
:math:`s_{\mathrm{z,0}}` über dem Boden befindet. Das Objekt kann beim
senkrechten Wurf nach unten somit maximal die Wegstrecke :math:`\Delta
s_{\mathrm{z,0}}` zurücklegen; erreicht es den Boden, so ist :math:`s(t)=0`:
Damit erhält man als Gleichung:

.. math::

    -z_0 = -v_0 \cdot t - \frac{1}{2} \cdot g \cdot t^2 \quad \Leftrightarrow
    \quad \frac{1}{2} \cdot g \cdot t^2 + v_0 \cdot t - z_0 = 0

Diese quadratische Gleichung für :math:`t_{\mathrm{max}}` kann folgendermaßen
mit Hilfe der Lösungsformel für quadratische Gleichungen gelöst werden:

.. math::

    t_{\mathrm{max}} = \frac{-v_0 + \sqrt{v_0^2 + 2 \cdot g \cdot z_0}}{g}

Setzt man diese Zeit :math:`t` in die Geschwindigkeit-Zeit-Gleichung ein, so
folgt für die Geschwindigkeit :math:`v` des Gegenstands unmittelbar vor dem
Aufprall auf den Boden:

.. math::

    v_{\mathrm{max}} &= -v_0 - g \cdot \left(\frac{-v_0 + \sqrt{v_0^2 + 2 \cdot g
    \cdot z_0}}{g}\right) \\[5pt]
    &= -v_0 \;\;\; - \;\; \big( -v_0 + \sqrt{v_0^2 + 2 \cdot g \cdot z_0}\big)
    \\[8pt]
    &= - \sqrt{v_0^2 + 2 \cdot g \cdot z_0}

Gilt im Speziellen für die Anfangsgeschwindigkeit :math:`v_0 = 0`, so entspricht
das Ergebnis :math:`v = \sqrt{2 \cdot g \cdot z_0}` der Geschwindigkeit des
Objekts beim freien Fall.


.. _Waagrechter Wurf:

Waagrechter Wurf
----------------

Wird ein Objekt von einer erhöhten Position :math:`s_{\mathrm{z,0}} = z_0`
aus waagrecht geworfen, so bewegt er sich -- unter Vernachlässigung des
Luftwiderstands -- entlang der horizontalen :math:`x`-Richtung mit seiner
ursprünglichen Geschwindigkeit :math:`v_{\mathrm{0}} = v_{\mathrm{x}}` fort. In
der vertikalen Richtung findet gleichzeitig eine gleichmäßig beschleunigte
Bewegung entgegen der :math:`z`-Achse statt; die Anfangsgeschwindigkeit in
dieser Richtung ist :math:`v_{\mathrm{z,0}} = 0`.

Für den Vektor :math:`\vec{v}` der Geschwindigkeit gilt somit in Abhängigkeit
von der Zeit :math:`t`:

.. math::

    \vec{v} = \begin{pmatrix} v_{\mathrm{x}} \\ v_{\mathrm{z}} \\ \end{pmatrix} =
    \begin{pmatrix} v_0 \\ - g \cdot t \end{pmatrix}

Die maximale Flugzeit :math:`t_{\mathrm{max}}` lässt sich aus der
:math:`z`-Komponente des zurückgelegten Weges bestimmen: Gilt :math:`s_{\mathrm{z}}
= 0`, so ist das Objekt auf dem Boden aufgekommen. Für die zugehörige Zeit
:math:`t_{\mathrm{max}}` gilt somit:

.. math::

    - \frac{1}{2} \cdot g \cdot t_{\mathrm{max}} + z_0 = 0 \quad
      \Leftrightarrow \quad t_{\mathrm{max}} = \sqrt{\frac{2 \cdot z_0}{g}}

Mit diesem Ergebnis lässt sich aus der :math:`x`-Komponente der Bewegung die
maximale Wurfweite :math:`s_{\mathrm{x,max}}` bestimmen:

.. math::

   s_{\mathrm{x,max}} = v_{\mathrm{0}} \cdot t_{\mathrm{max}} = v_0  \cdot \sqrt{\frac{2
   \cdot z_{\mathrm{0}}}{g}}


.. _Schräger Wurf:

Schräger Wurf
-------------

Bei einem schrägen Wurf wird ein Objekt  in einem Winkel :math:`\alpha`
gegenüber der Horizontalen abgeworfen :math:`(0 < \alpha < 90\degree)`.
Für die Komponenten :math:`v_{\mathrm{\mathrm{0x}}}` und :math:`v_{\mathrm{0z}}`
der Geschwindigkeit :math:`v_0` des Objekts gilt beim Abwurf:

.. math::

    \vec{v}_0 = \begin{pmatrix}
    v_{\mathrm{\mathrm{0x}}} \\
    v_{\mathrm{0z}} \\
    \end{pmatrix} = \begin{pmatrix}
    v_0 \cdot \cos{(\alpha)}\\
    v_0 \cdot \sin{(\alpha})\\
    \end{pmatrix}

Ohne Luftwiderstand bleibt die horizontale Komponente der Geschwindigkeit
unverändert. In vertikaler Richtung wird das Objekt hingegen -- wie beim
senkrechten Wurf nach oben -- mit der Beschleunigung :math:`g=\unit[9,81]{m/s^2}`
zum Erdmittelpunkt hin beschleunigt. Für die Geschwindigkeit :math:`\vec{v}`
gilt somit in Abhängigkeit von der Zeit :math:`t`:

.. math::

    \vec{v}(t) = \begin{pmatrix}
    v_{\mathrm{x}}\\
    v_{\mathrm{z}} \\
    \end{pmatrix}
    = \begin{pmatrix}
    v_{\mathrm{\mathrm{0x}}} \\
    v_{\mathrm{0z}} - g \cdot t
    \end{pmatrix}

Es findet also eine Überlagerung einer Bewegung mit konstanter Geschwindigkeit
in :math:`x`-Richtung und einer Bewegung mit konstanter Beschleunigung in
:math:`z`-Richtung statt. Für die in beiden Richtungen zurückgelegten
Wegstrecken :math:`\Delta s_{\mathrm{x}}` und :math:`\Delta s_{\mathrm{y}}` gilt:

.. math::

    \Delta \vec{s} = \begin{pmatrix}
    \Delta s_{\mathrm{x}}\\
    \Delta s_{\mathrm{z}} \\
    \end{pmatrix}
    = \begin{pmatrix}
    v_{\mathrm{0x}} \cdot t \\
    v_{\mathrm{0z}} \cdot t - \frac{1}{2} \cdot g \cdot t^2
    \end{pmatrix}

Im Folgenden wird wiederum zunächst angenommen, dass das Objekt aus einer Höhe
:math:`s_{\mathrm{0z}} = \unit[0]{m}` geworfen wird. Wie beim senkrechten Wurf
gilt dann für die Zeit :math:`t`, in welcher der Körper die maximale Steighöhe
:math:`s_{\mathrm{z,max}}` erreicht:

.. math::

    v_{\mathrm{0z}} - g \cdot t_{\mathrm{z,max}} = 0 \quad \Leftrightarrow \quad
    t_{\mathrm{z,max}} = \frac{v_{\mathrm{0z}}}{g}

Setzt man diese Zeit in die Bewegungsgleichung für die :math:`z`-Komponente
ein, so folgt für die maximale Steighöhe :math:`s_{\mathrm{z,max}}`:

.. math::

    s_{z,\mathrm{max}} = v_{\mathrm{0z}} \cdot \frac{v_{\mathrm{0z}}}{g} - \frac{1}{2}
    \cdot g \cdot \left( \frac{v_{\mathrm{0z}}}{g} \right)^2 = \frac{v_{\mathrm{0z}}^2}{g} -
    \frac{1}{2} \cdot g \cdot \frac{v_{\mathrm{0z}}^2}{g^2} = \frac{v_{\mathrm{0z}}^2}{2 \cdot g}

..  Wird der Gegenstand aus einer Höhe :math:`h=0` abgeworfen, so ist die Wurfweite
..  am höchsten, wenn :math:`\alpha = 45\degree` ist. Die Wurfweite :math:`s_{\mathrm{x}}`
..  beträgt in diesem Fall

Die Wurfbahn ist (ohne Luftwiderstand) parabelförmig und damit symmetrisch; die
Zeit bis zum Aufprall auf dem Boden muss somit doppelt so lang sein wie die Zeit
:math:`t_{\mathrm{z,max}}` zum Erreichen der maximalen Steighöhe. In dieser Zeit
erreicht das Objekt in horizontaler Richtung folgende Entfernung:

.. math::

    s_{\mathrm{x,max}} = v_{\mathrm{0x}} \cdot (2 \cdot t_{\mathrm{z,max}}) = v_0 \cdot
    \cos{\alpha} \cdot 2 \cdot \frac{v_0 \cdot \sin{\alpha}}{g} = \frac{v_0^2
    \cdot 2 \cdot \sin{\alpha} \cdot \cos{\alpha}}{g} = \frac{v_{\mathrm{0}}^2
    \cdot \sin{(2 \cdot \alpha)}}{g}

Hierbei wurde im letzten Rechenschritt das Additionstheorem für Sinus-Funktionen
genutzt. Die Wurfweite ist also -- ebenfalls wie die Wurfhöhe -- vom
Wurfwinkel :math:`\alpha` abhängig. Für :math:`\alpha = 45\degree` ist im
obigen Fall :math:`\sin{(2 \cdot \alpha)} = \sin{(90 \degree)} = 1` und somit die
Wurfweite maximal :math:`(s_{\mathrm{x \, max,45\degree}} = \frac{v_0^2}{g})`.


















