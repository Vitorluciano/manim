from manim import *


class Trig(Scene):
    def construct(self):
        #PARTE 1: APRESENTAÇÃO DO TRIÂNGULO RETÂNGULO E SEUS ELEMENTOS
        #instancia os vértices do triângulo
        A = Dot(point=ORIGIN, radius=0.05)
        B = Dot(point=2*RIGHT, radius=0.05)
        C = Dot(point=2*(RIGHT + UP), radius=0.05)

        #desenha os vértices do triangulo
        self.play(AnimationGroup(Write(A), Write(B), Write(C), lag_ratio=0.25), run_time=1.5)

        def line_updater(P1, P2):
            """Retorna uma função que atualiza um segmento de reta a partir dos seus pontos extremos"""
            return lambda x: x.become(Line(start=P1.get_center(), end=P2.get_center()))
        
        #instancia os segmentos de reta (lados) do triangulo retângulo
        hipotenusa = Line()
        c_adjacente = Line()
        c_oposto = Line()

        #agrupa os lados em um único objeto para que possam ser manipulados em conjunto
        lados = VGroup(c_adjacente, c_oposto, hipotenusa)

        #adiciona o updater para que as retas sejam atualizadas juntos com os pontos
        hipotenusa.add_updater(line_updater(C, A))
        c_adjacente.add_updater(line_updater(A, B))
        c_oposto.add_updater(line_updater(B, C))

        #desenha as retas
        self.play(Write(lados, lag_ratio=0.5), run_time=1.5)

        #instancia os angulos reto e theta
        #ATENÇÃO: TALVEZ SEJA MELHOR USAR UM UPDATER PARA THETA
        reto = RightAngle(c_adjacente, c_oposto, length=0.4, quadrant=(-1, 1), color=RED)
        reto.depth = -1
        theta = Angle.from_three_points(B, A, C, radius=0.5)

        #desenha o ângulo reto para evidenciar que estamos trabalhando com um triângulo retângulo
        #ATENÇÃO: EU PRECISA REPRESENTÁ-LO COMO UM ÂNGULO RETO
        self.play(FadeIn(reto))

        #apaga o ângulo reto para evitar poluição visual
        self.play(FadeOut(reto))

        #desenha o ângulo theta   
        self.play(Write(theta))

        #instancia labels para os elementos que queremos destacar
        hip_label = Tex("hipotenusa", font_size=30)
        ca_label = Tex("cateto adjacente", font_size=30)
        co_label = Tex("cateto oposto", font_size=30)
        theta_label = MathTex(r"\theta", font_size=30) #ATENÇÃO: PRECISO SUBSTITUIR A LETRA T POR θ

        #adiciona um updater para que as labels estejam sempre próximas dos seus respectivos elementos
        hip_label.add_updater(lambda x: x.next_to(hipotenusa, 0.1*LEFT))
        ca_label.add_updater(lambda x: x.next_to(c_adjacente, DOWN))
        co_label.add_updater(lambda x: x.next_to(c_oposto, RIGHT))
        theta_label.add_updater(lambda x: x.next_to(theta)) #ATENÇÃO: PRECISO MELHORAR A POSIÇÃO DA THETA_LABEL

        #agrupa as labels em um único objeto para que possam ser manipuladas em conjunto
        labels = VGroup(hip_label, ca_label, co_label, theta_label)

        #faz as labels surgirem gradualmente
        for label in labels:
            self.play(FadeIn(label))

        #transforma labels longas em labels mais simples
        self.play(ReplacementTransform(hip_label, Tex("hip").next_to(hipotenusa, 0.1*LEFT)))
        self.play(ReplacementTransform(ca_label, Tex("ca").next_to(c_adjacente, DOWN)))
        self.play(ReplacementTransform(co_label, Tex("co").next_to(c_oposto, RIGHT)))

        #PARTE 2: DEFINIÇÃO DE SENO E COSSENO
        seno = MathTex(r"sin(\theta) = \frac{co}{hip}").move_to(5*LEFT + UP)
        cosseno = MathTex(r"cos(\theta) = \frac{ca}{hip}").move_to(5*LEFT + DOWN)

        #escreve as definições de seno e cosseno
        self.play(Write(seno), Write(cosseno), run_time=2)



