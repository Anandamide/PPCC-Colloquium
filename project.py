from manim import*
import math

class Opening (Scene):
    def construct(self):
        title1 = Text("Covectors, differential forms ").move_to(UP*1.7).scale(1.3)
        title2 = Text("and a new interpretation").next_to(title1,DOWN*1.1).scale(1.3)
        title3 = Text("of the definite integral").next_to(title2,DOWN*1.1).scale(1.3)
        name = Text("Jordan Jacobson").next_to(title3,DOWN*1.2).scale(0.8)
        self.play(ShowCreation(title1),ShowCreation(title2),ShowCreation(title3),ShowCreation(name))
        self.wait(10)
        self.play(Uncreate(title1),Uncreate(title2),Uncreate(title3),Uncreate(name))

class Scene1 (GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-1.5,
            x_max=3.5,
            x_axis_width=7,
            num_graph_anchor_points=100,
            y_min=-3,
            y_max=6,
            graph_origin=LEFT*4.5,
            axes_color=WHITE,
            x_labeled_nums=range(-1,4, 1),
            y_labeled_nums=range(-3,7, 1),
            y_axis_height=4.5,
            **kwargs
        )
        self.function_color = RED
    def construct(self):

        title = Text("A quick refresher on the definite integral...")
        self.play(ShowCreation(title))
        self.wait(2)
        self.play(Uncreate(title))

        self.setup_axes(animate=True)
        func1 =self.get_graph(lambda x: 4- 2*x,
                                    x_min=-1,
                                    x_max=3)
        func2 =self.get_graph(lambda x: 4*x- x**2 +2,
                                    x_min=-1,
                                    x_max=3)

        f = self.get_graph_label(func1, label="f(x)=4-2x")
        labelf = MathTex(r"f(x)=4-2x")
        riemann1 = MathTex(r"A \approx \sum_{i=1}^{n} f(x_i^*)\Delta x").move_to(RIGHT*4)
        riemann2 = MathTex(r"A = \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\Delta x)")
        riemann3 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x; n=4,\Delta x=1\\ &\approx 4").move_to(UP*2.5+RIGHT*3)
        riemann4 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x; n=8,\Delta x=\frac{1}{2}\\ &\approx 6").move_to(UP*2.5+RIGHT*3)
        riemann5 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x; n=16,\Delta x=\frac{1}{4}\\ &\approx 7").move_to(UP*2.5+RIGHT*3)
        riemann6 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x; n=32,\Delta x=\frac{1}{8}\\ &\approx 7.5").move_to(UP*2.5+RIGHT*3)
        riemann7 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x; n=64,\Delta x=\frac{1}{16}\\ &\approx 7.75").move_to(UP*2.5+RIGHT*3)
        riemann8 = MathTex(r"A &= \lim_{n\to\infty} \sum_{i=1}^{n} f(x_i^*)\Delta x\\&=\int_{-1}^{3} (4-2x) dx").move_to(UP*2.5+RIGHT*3)
        integ = MathTex(r"A &=\int_{-1}^{3} (4-2x) dx \\&=4x-x^2 \vert_{-1}^{3} \\&=(12-9)-(-4-1) \\&= 3+5 \\&=8").move_to(UP*1.2+RIGHT*4)


        blinev = self.get_vertical_line_to_graph(3,func1)
        blineh = Line(self.coords_to_point(2,-2),self.coords_to_point(3,-2))
        blinev.set_opacity(0)
        blineh.set_opacity(0)

        b1 = Brace(blinev,direction=RIGHT)
        b2 = Brace(blineh,direction=DOWN)


        b1text = b1.get_tex("f(x)")
        b2text = b2.get_tex("\Delta x")


        area = self.get_area(func1,-1,3,area_color="#ADADAD")
        r1 = self.get_riemann_rectangles(func1,-1,3,dx=1, input_sample_type='right', stroke_width=1, stroke_color='#000000', fill_opacity=0.5)
        r2 = self.get_riemann_rectangles(func1,-1,3,dx=0.5, input_sample_type='right', stroke_width=1, stroke_color='#000000', fill_opacity=0.5)
        r3 = self.get_riemann_rectangles(func1,-1,3,dx=0.25, input_sample_type='right', stroke_width=1, stroke_color='#000000', fill_opacity=0.5)
        r4 = self.get_riemann_rectangles(func1,-1,3,dx=0.125, input_sample_type='right', stroke_width=1, stroke_color='#000000', fill_opacity=0.5)
        r5 = self.get_riemann_rectangles(func1,-1,3,dx=0.0625, input_sample_type='right', stroke_width=1, stroke_color='#000000', fill_opacity=0.5)
        r6 = self.get_riemann_rectangles(func1,-1,3,dx=0.005, input_sample_type='right', stroke_width=0, stroke_color='#000000', fill_opacity=0.5)



        lowerbound = self.get_vertical_line_to_graph(-1,func1,DashedLine,color=YELLOW)
        upperbound = self.get_vertical_line_to_graph(3,func1,DashedLine,color=YELLOW)

        self.play(ShowCreation(func1),ShowCreation(f))
        self.wait(2)
        self.play(FadeOut(f),ShowCreation(r1),ShowCreation(riemann1),
                  ShowCreation(b1),ShowCreation(b2),ShowCreation(blineh),
                  ShowCreation(blinev),ShowCreation(b1text),ShowCreation(b2text),
                  ShowCreation(lowerbound),ShowCreation(upperbound))
        self.wait(2)
        self.play(Transform(riemann1,riemann3))
        self.wait(2)
        self.play(FadeOut(b1),FadeOut(b2),FadeOut(b1text),FadeOut(b2text),
                  Transform(riemann1,riemann4),Transform(r1,r2))
        self.wait(2)
        self.play(Transform(riemann1,riemann5),Transform(r1,r3))
        self.wait(2)
        self.play(Transform(riemann1,riemann6),Transform(r1,r4))
        self.wait(2)
        self.play(Transform(riemann1,riemann7),Transform(r1,r5))
        self.wait(2)
        self.play(Transform(riemann1,riemann8),Transform(r1,r6))
        self.wait(4)
        self.play(Transform(riemann1,integ))
        self.wait(2)



        integ2 = MathTex(r"\int_{-1}^{3}","(4-2x)","dx").scale(2).move_to(LEFT*1.5+UP)
        integ3 = MathTex(r"\int_{-1}^{3}","(4-2x)dx").scale(2).move_to(LEFT*1.5+UP)

        b3 = Brace(integ2[1],direction=DOWN)
        b4 = Brace(integ2[2],direction=RIGHT)
        b5 = Brace(integ3[1],direction=DOWN)

        b3text = b3.get_text('integrand')
        b4text = b4.get_text('infinitesimal')
        b5text = b5.get_text('covector')

        self.play(Uncreate(self.axes),Uncreate(func1),Uncreate(r1),Uncreate(lowerbound),Uncreate(upperbound))
        self.play(Transform(riemann1,integ2),FadeIn(b3),FadeIn(b3text),FadeIn(b4),FadeIn(b4text))
        self.wait(4)
        self.remove(riemann1)
        self.add(integ3)
        self.play(Transform(b3,b5),Transform(b3text,b5text), FadeOut(b4),FadeOut(b4text))
        self.wait(2)
        self.play(FadeOut(b3),FadeOut(b3text),FadeOut(integ3))
        self.wait(2)

        integ4 = MathTex(r"\int f(x)dx =","F(x)"," + c").move_to(UP)
        b6 = Brace(integ4[1],direction=DOWN)
        b6text = b6.get_text('Scalar potential')

        pot1 = MathTex(r"\frac{dF}{dx} = f(x)")
        pot2 = MathTex(r"f(x)dx","= \\frac{df}{dx}dx"," =dF").move_to(UP)
        integ5 = MathTex(r"\int_a^b f(x)dx").next_to(pot2, DOWN)
        integ6 = MathTex(r"\int_a^b","dF").next_to(pot2, DOWN)
        integ7 = MathTex(r"A &= \int_a^b dF \\ &=F\vert_a^b \\ &= F(b)-F(a)")

        self.play(ShowCreation(integ4))
        self.play(FadeIn(b6),FadeIn(b6text))
        self.wait(2)
        self.play(Transform(integ4,pot1),FadeOut(b6),FadeOut(b6text))
        self.wait(2)
        self.play(Transform(integ4,pot2),FadeIn(integ5))
        self.wait(2)
        self.play(Transform(integ5, integ6))
        self.wait(2)
        self.play(FadeOut(integ4), Transform(integ5, integ7))
        self.wait(5)
class Scene2 (GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=7,
            x_axis_width=7,
            num_graph_anchor_points=100,
            y_min=0,
            y_max=6,
            graph_origin=LEFT*4 +DOWN*3,
            axes_color=WHITE,
            x_labeled_nums=range(0,8, 1),
            y_labeled_nums=range(0,7, 1),
            y_axis_height=6,
            **kwargs
        )
        self.function_color = RED
    def construct(self):
        text1 = Text("So what is a covector?").scale(1.2).move_to(UP*1.5)
        text2 = Text("Before we can answer that").next_to(text1,DOWN*1.5)
        text3 = Text("we should quickly talk about vectors").next_to(text2,DOWN)

        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2),Write(text3))
        self.wait(3)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))

        v1 = Arrow(start=[-2,-1, 0], end=[2, 2, 0], color=BLUE,buff=0)
        v2 = Arrow(start=[-2,-1, 0], end=[3, 0, 0], color=PURPLE,buff=0)
        v3 = Arrow(start=[3, 0, 0], end=[2, 2, 0], color=GREEN,buff=0)
        v4 = Arrow(start=[-2,-1,0], end=[4, 3.5, 0], color=BLUE, buff=0)
        v5 = v1.copy()
        text4 = MathTex(r"\vec v", "=",r"\vec u", "+", r"\vec w").next_to(v1,DOWN*1.5)
        text6 = Text("Vector Addition").next_to(text4,DOWN)

        text4[0].set_color(color=BLUE)
        text4[2].set_color(color=GREEN)
        text4[4].set_color(color=PURPLE)

        line = Line([-2,-1, 0],[2, 2, 0])
        b1 = BraceBetweenPoints([-2,-1, 0],[2, 2, 0])
        b1text = b1.get_tex(r"||",r"\vec v","||")
        b1text[1].set_color(color=BLUE)
        b2 = BraceBetweenPoints([-2,-1,0],[4,3.5,0])
        b2text = b2.get_tex(r"n||",r"\vec v","||")
        b2text[1].set_color(color=BLUE)
        text5 = MathTex (r"n",r"\vec v",).next_to(v1,DOWN*1.5)
        text7 = Text ("Scalar Multiplication").next_to(text5,DOWN)
        text5[1].set_color(color=BLUE)

        self.play(ShowCreation(v1))
        self.wait(3)
        self.play(ShowCreation(b1), Write(b1text))
        self.wait(2)
        self.play(Write(text7), Write(text5), ReplacementTransform(v1,v4),ReplacementTransform(b1,b2),ReplacementTransform(b1text,b2text))
        self.wait(2)
        self.play(Uncreate(b2),Uncreate(b2text),Uncreate(text5),Uncreate(text7),ReplacementTransform(v4,v5))
        self.wait(2)
        self.play(ShowCreation(v2),ShowCreation(v3),Write(text4),Write(text6))
        self.wait(2)
        self.play(Uncreate(v5),Uncreate(v2),Uncreate(v3),Uncreate(text4),Uncreate(text6))

        v1 = Arrow(start=[-2,-1, 0], end=[2, 2, 0], color=BLUE,buff=0)
        v2 = Arrow(start=[-2,-1, 0], end=[3, 0, 0], color=PURPLE,buff=0)
        v3 = Arrow(start=[3, 0, 0], end=[2, 2, 0], color=GREEN,buff=0)
        v4 = Arrow(start=[-2,-1,0], end=[4, 3.5, 0], color=BLUE, buff=0)
        v5 = Arrow(start=[-2,-1, 0], end=[5.5, 0.5, 0], color=PURPLE,buff=0)
        v6 = Arrow(start=[5.5, 0.5, 0], end=[4, 3.5, 0], color=GREEN,buff=0)

        b4=BraceBetweenPoints([4, 3.5, 0], [-2,-1, 0])
        b5=BraceBetweenPoints([-2,-1, 0], [5.5, 0.5, 0])
        b6=BraceBetweenPoints([5.5, 0.5, 0], [4, 3.5, 0])

        text8 = Text("Scalar Multiplication distributes")
        text82 = Text("over vector addition").next_to(text8,DOWN)
        text9 = MathTex(r"n(",r"\vec u","+",r"\vec w)","=n",r"\vec u","+n",r"\vec w").next_to(text82,DOWN)
        text9[1].set_color(color=GREEN)
        text9[3].set_color(color=PURPLE)
        text9[5].set_color(color=GREEN)
        text9[7].set_color(color=PURPLE)
        text10 = text9.copy().next_to(v1,DOWN*2)


        v4text = b4.get_tex(r"n",r"\vec v")
        v5text = b5.get_tex(r"n",r"\vec w")
        v6text = b6.get_tex(r"n",r"\vec u")
        v4text[1].set_color(color=BLUE)
        v5text[1].set_color(color=PURPLE)
        v6text[1].set_color(color=GREEN)
        self.play(Write(text8),Write(text82),Write(text9))
        self.wait(2)
        self.play(Transform(text9,text10),FadeOut(text8),FadeOut(text82),ShowCreation(v1),ShowCreation(v2),ShowCreation(v3))
        self.wait()
        self.play(Transform(v1,v4),Transform(v2,v5),Transform(v3,v6),Write(v4text),Write(v5text),Write(v6text),
                  ShowCreation(b4),ShowCreation(b5),ShowCreation(b6))
        self.wait(2)
        self.play(FadeOut(v1),FadeOut(v2),FadeOut(v3),FadeOut(b4),FadeOut(b5),FadeOut(b6),FadeOut(v4text),
                  FadeOut(v5text),FadeOut(v6text),FadeOut(text9))
        self.wait()

        text11 = Text("With these two operations,").move_to(UP*2)
        text12 = Text("scalar multiplication and vector addition,").next_to(text11,DOWN)
        text13 = Text("along with a set of vectors and scalars,").next_to(text12,DOWN)
        text14 = Text("we have a vector space denoted V.").next_to(text13,DOWN)

        self.play(Write(text11),Write(text12),Write(text13),Write(text14))
        self.wait(2)

        text15 = Text("At no point have we mentioned a").move_to(UP*0.5)
        text16 = Text("coordinate system or basis.").next_to(text15,DOWN)

        self.play(Transform(text11,text15),Transform(text12,text16),
                  FadeOut(text13),FadeOut(text14))
        self.wait(2)

        text17 = Text("Vectors are geometric objects that").move_to(UP*0.75)
        text18 = Text("are independent of a coordinate system").next_to(text17,DOWN)
        text19 = Text("or a basis.").next_to(text18,DOWN)

        self.play(Transform(text11,text17),Transform(text12,text18),
              Write(text19))
        self.wait(2)

        text20 = Text("Given a basis, a vector can be written as").move_to(UP*1.2)
        text21 = Text("a linear combination of the basis vectors.").next_to(text20,DOWN)
        text22 = MathTex(r"\textrm {Basis: }",r"\vec e^{\, 0}",",",r"\vec e^{\, 1}",",...,",r"\vec e^{\, i}").next_to(text21,DOWN*1.2).scale(1.5)
        text23 = MathTex(r"\vec v","=","v_0",r"\vec e^{\,0}","+","v_1",r"\vec e^{\,1}","+...+","v_i",r"\vec e^{\,i}").next_to(text22,DOWN).scale(1.5)

        text22[1].set_color(color=GREEN)
        text22[3].set_color(color=GREEN)
        text22[5].set_color(color=GREEN)

        text23[0].set_color(color=PURPLE)
        text23[2].set_color(color=PURPLE)
        text23[3].set_color(color=GREEN)
        text23[5].set_color(color=PURPLE)
        text23[6].set_color(color=GREEN)
        text23[8].set_color(color=PURPLE)
        text23[9].set_color(color=GREEN)

        self.play(Transform(text11,text20),Transform(text12,text21),Transform(text19,text22),
                  Write(text23))
        self.wait(4)
        self.play(FadeOut(text11), FadeOut(text12), FadeOut(text19), FadeOut(text23))

        def polar2c(p):
            return np.array([
                p[0]*np.cos(p[1]),
                p[0]*np.sin(p[1]),
                0
                ])

        text24 = Text("The orthonormal basis in \mathbb{R}^2 is:").move_to(UP)
        text25 = MathTex(r"\vec e^{\, x}",",",r"\vec e^{\, y}").next_to(text24,DOWN)
        text25[0].set_color(color=GREEN)
        text25[2].set_color(color=GREEN)

        vcomp = MathTex("1",r"\vec e^{\, x}","+","2",r"\vec e^{\, y}")
        vcomp[0].set_color(color=BLUE)
        vcomp[1].set_color(color=GREEN)
        vcomp[3].set_color(color=BLUE)
        vcomp[4].set_color(color=GREEN)

        grid=NumberPlane().set_color(color="#878787")

        ex = Arrow([0,0,0],[1,0,0],color=GREEN,buff=0)
        ey = Arrow([0,0,0],[0,1,0],color=GREEN,buff=0)
        exlabel = MathTex(r"\vec e^{\,x}").set_color(color=GREEN).next_to(ex,DOWN)
        eylabel = MathTex(r"\vec e^{\,y}").set_color(color=GREEN).next_to(ey,LEFT)

        self.play(ShowCreation(grid),ShowCreation(ex),ShowCreation(ey),Write(exlabel),Write(eylabel))
        self.wait(2)
        self.play(FadeOut(exlabel),FadeOut(eylabel))

        v = Arrow([0,0,0],[1,2,0],color=BLUE,buff=0)
        vtext=MathTex(r"\vec v","=").move_to(LEFT*3 +UP*2)
        vtext[0].set_color(color=BLUE)
        vm = Matrix([[1],[2]],left_bracket="\\big(",right_bracket="\\big)").next_to(vtext,RIGHT).set_color(BLUE)
        vex = ex.copy()
        vey = Arrow([1,0,0],[1,2,0],color=GREEN,buff=0)
        vxb = Brace(vex)
        vyb = Brace(vey,RIGHT)
        vxlabel = vxb.get_tex("1",r"\vec e^{\,x}")
        vylabel = vyb.get_tex("2",r"\vec e^{\,y}")
        vxlabel[0].set_color(color=BLUE)
        vxlabel[1].set_color(color=GREEN)
        vylabel[0].set_color(color=BLUE)
        vylabel[1].set_color(color=GREEN)

        v2 = Arrow([0,0,0],[3,-3,0],color=BLUE,buff=0)
        v2text=MathTex(r"\vec v","=").move_to(LEFT*3 +UP*2)
        v2text[0].set_color(color=BLUE)
        v2m = Matrix([[3],[-3]],left_bracket="\\big(",right_bracket="\\big)").next_to(vtext,RIGHT).set_color(BLUE)
        v2ex = Arrow([0,0,0],[3,0,0],color=GREEN,buff=0)
        v2ey = Arrow([3,0,0],[3,-3,0],color=GREEN,buff=0)
        v2xb = Brace(v2ex,UP)
        v2yb = Brace(v2ey,RIGHT)
        v2xlabel = v2xb.get_tex("3",r"\vec e^{\,x}")
        v2ylabel = v2yb.get_tex("-3",r"\vec e^{\,y}")
        v2xlabel[0].set_color(color=BLUE)
        v2xlabel[1].set_color(color=GREEN)
        v2ylabel[0].set_color(color=BLUE)
        v2ylabel[1].set_color(color=GREEN)

        v3 = Arrow([0,0,0],[4,3,0],color=BLUE,buff=0)
        v3text=MathTex(r"\vec v","=").move_to(LEFT*3 +UP*2)
        v3text[0].set_color(color=BLUE)
        v3m = Matrix([[4],[3]],left_bracket="\\big(",right_bracket="\\big)").next_to(vtext,RIGHT).set_color(BLUE)
        v3ex = Arrow([0,0,0],[4,0,0],color=GREEN,buff=0)
        v3ey = Arrow([4,0,0],[4,3,0],color=GREEN,buff=0)
        v3xb = Brace(v3ex,DOWN)
        v3yb = Brace(v3ey,RIGHT)
        v3xlabel = v3xb.get_tex("4",r"\vec e^{\,x}")
        v3ylabel = v3yb.get_tex("3",r"\vec e^{\,y}")
        v3xlabel[0].set_color(color=BLUE)
        v3xlabel[1].set_color(color=GREEN)
        v3ylabel[0].set_color(color=BLUE)
        v3ylabel[1].set_color(color=GREEN)

        self.play(GrowFromCenter(v),Transform(ey,vey),ShowCreation(vxb),
                  ShowCreation(vyb),Write(vxlabel),Write(vylabel),Write(vtext),Write(vm))
        self.wait(2)
        self.play(Transform(v,v2),Transform(ex,v2ex),Transform(ey,v2ey),Transform(vxb,v2xb),
                  Transform(vyb,v2yb),Transform(vxlabel,v2xlabel),Transform(vylabel,v2ylabel),
                  Transform(vm,v2m),Transform(vtext,v2text))
        self.wait(2)
        self.play(Transform(v,v3),Transform(ex,v3ex),Transform(ey,v3ey),Transform(vxb,v3xb),
                  Transform(vyb,v3yb),Transform(vxlabel,v3xlabel),Transform(vylabel,v3ylabel),
                  Transform(vm,v3m),Transform(vtext,v3text))
        self.wait(2)
        self.play(Transform(ex,Arrow([0,0,0],[1,0,0],color=GREEN,buff=0)),Transform(ey,Arrow([0,0,0],[0,1,0],color=GREEN,buff=0)),FadeOut(vxb),FadeOut(vyb),FadeOut(vxlabel),FadeOut(vylabel),
                  FadeOut(vm),FadeOut(vtext),Write(exlabel),Write(eylabel))
        self.wait()

        e2x = Arrow([0,0,0],[2,0,0],color=RED,buff=0)
        e2y = Arrow([0,0,0],[0,2,0],color=RED,buff=0)
        v4x = Arrow([0,0,0],[4,0,0],color=RED,buff=0)
        v4y = Arrow([4,0,0],[4,3,0],color=RED,buff=0)
        v4text=MathTex(r"\vec v","=").move_to(LEFT*3 +UP*2)
        v4text[0].set_color(color=BLUE)
        v4m = Matrix([[2],[1.5]],left_bracket="\\big(",right_bracket="\\big)").next_to(vtext,RIGHT).set_color(BLUE)
        v4xb = Brace(v4x,DOWN)
        v4yb = Brace(v4y,RIGHT)
        v4xblabel = v4xb.get_tex("2",r"\bar e^{\,x}")
        v4yblabel = v4yb.get_tex(r"\frac{3}{2}",r"\bar e^{\,y}")
        v4xblabel[1].set_color(color=RED)
        v4yblabel[1].set_color(color=RED)
        e2xlabel = MathTex(r"\bar e^{\,x}").set_color(color=RED).next_to(e2x,DOWN)
        e2ylabel = MathTex(r"\bar e^{\,y}").set_color(color=RED).next_to(e2y,RIGHT)
        text26 = MathTex(r"\bar e^{\,x}","=2",r"\vec e^{\,x}").move_to(LEFT*3+DOWN*2.5)
        text27 = MathTex(r"\bar e^{\,y}","=2",r"\vec e^{\,y}").next_to(text26,DOWN)
        text26[0].set_color(color=RED)
        text26[2].set_color(color=GREEN)
        text27[0].set_color(color=RED)
        text27[2].set_color(color=GREEN)


        grid2 = NumberPlane(x_line_frequency=2,y_line_frequency=2)
        self.play(Transform(grid,grid2),Transform(ex,e2x),Transform(ey,e2y),Transform(exlabel,e2xlabel),Transform(eylabel,e2ylabel),
                  Write(text26),Write(text27))
        self.wait()
        self.play(Write(v4text),Write(v4m),Transform(ex,v4x),Transform(ey,v4y),ShowCreation(v4xb),ShowCreation(v4yb),Transform(exlabel,v4xblabel),Transform(eylabel,v4yblabel))
        self.wait()
