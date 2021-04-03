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
        riemann3 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x;\, n=4,\Delta x=1\\ &\approx 4").move_to(UP*2.5+RIGHT*3)
        riemann4 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x;\, n=8,\Delta x=\frac{1}{2}\\ &\approx 6").move_to(UP*2.5+RIGHT*3)
        riemann5 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x;\, n=16,\Delta x=\frac{1}{4}\\ &\approx 7").move_to(UP*2.5+RIGHT*3)
        riemann6 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x;\, n=32,\Delta x=\frac{1}{8}\\ &\approx 7.5").move_to(UP*2.5+RIGHT*3)
        riemann7 = MathTex(r"A &\approx \sum_{i=1}^{n} f(x_i^*)\Delta x;\, n=64,\Delta x=\frac{1}{16}\\ &\approx 7.75").move_to(UP*2.5+RIGHT*3)
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
        self.wait(3)
        self.play(Transform(riemann1,riemann3))
        self.wait(3)
        self.play(FadeOut(b1),FadeOut(b2),FadeOut(b1text),FadeOut(b2text),
                  Transform(riemann1,riemann4),Transform(r1,r2))
        self.wait(3)
        self.play(Transform(riemann1,riemann5),Transform(r1,r3))
        self.wait(3)
        self.play(Transform(riemann1,riemann6),Transform(r1,r4))
        self.wait(3)
        self.play(Transform(riemann1,riemann7),Transform(r1,r5))
        self.wait(3)
        self.play(Transform(riemann1,riemann8),Transform(r1,r6))
        self.wait(3)
        self.play(Transform(riemann1,integ))
        self.wait(3)



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
        self.wait(3)
        self.play(Transform(integ4,pot1),FadeOut(b6),FadeOut(b6text))
        self.wait(3)
        self.play(Transform(integ4,pot2),FadeIn(integ5))
        self.wait(3)
        self.play(Transform(integ5, integ6))
        self.wait(3)
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
        text4 = MathTex(r"\vec v", "=",r"\vec u", "+", r"\vec w").next_to(v1,DOWN*1.5).scale(1.5)
        text6 = Text("Vector Addition").next_to(text4,DOWN).scale(0.9)

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
        text5 = MathTex (r"n",r"\vec v",).next_to(v1,DOWN*1.5).scale(1.5)
        text7 = Text ("Scalar Multiplication").next_to(text5,DOWN).scale(0.9)
        text5[1].set_color(color=BLUE)

        self.play(ShowCreation(v1))
        self.wait(3)
        self.play(ShowCreation(b1), Write(b1text))
        self.wait(3)
        self.play(Write(text7), Write(text5), ReplacementTransform(v1,v4),ReplacementTransform(b1,b2),ReplacementTransform(b1text,b2text))
        self.wait(3)
        self.play(Uncreate(b2),Uncreate(b2text),Uncreate(text5),Uncreate(text7),ReplacementTransform(v4,v5))
        self.wait(3)
        self.play(ShowCreation(v2),ShowCreation(v3),Write(text4),Write(text6))
        self.wait(3)
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
        text9 = MathTex(r"n(",r"\vec u","+",r"\vec w)","=n",r"\vec u","+n",r"\vec w").next_to(text82,DOWN).scale(1.5)
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
        self.wait(3)
        self.play(Transform(text9,text10),FadeOut(text8),FadeOut(text82),ShowCreation(v1),ShowCreation(v2),ShowCreation(v3))
        self.wait()
        self.play(Transform(v1,v4),Transform(v2,v5),Transform(v3,v6),Write(v4text),Write(v5text),Write(v6text),
                  ShowCreation(b4),ShowCreation(b5),ShowCreation(b6))
        self.wait(3)
        self.play(FadeOut(v1),FadeOut(v2),FadeOut(v3),FadeOut(b4),FadeOut(b5),FadeOut(b6),FadeOut(v4text),
                  FadeOut(v5text),FadeOut(v6text),FadeOut(text9))
        self.wait()

        text11 = Text("With these two operations,").move_to(UP*2)
        text12 = Text("scalar multiplication and vector addition,").next_to(text11,DOWN)
        text13 = Text("along with a set of vectors and scalars,").next_to(text12,DOWN)
        text14 = Text("we have a vector space denoted V.").next_to(text13,DOWN)

        self.play(Write(text11),Write(text12),Write(text13),Write(text14))
        self.wait(4)

        text15 = Text("At no point have we mentioned a").move_to(UP*0.5)
        text16 = Text("coordinate system or basis.").next_to(text15,DOWN)

        self.play(Transform(text11,text15),Transform(text12,text16),
                  FadeOut(text13),FadeOut(text14))
        self.wait(3)

        text17 = Text("Vectors are geometric objects that").move_to(UP*0.75)
        text18 = Text("are independent of a coordinate system").next_to(text17,DOWN)
        text19 = Text("or a basis.").next_to(text18,DOWN)

        self.play(Transform(text11,text17),Transform(text12,text18),
              Write(text19))
        self.wait(3)

        text20 = Text("Given a basis, a vector can be written as").move_to(UP*1.2)
        text21 = Text("a linear combination of the basis vectors.").next_to(text20,DOWN)
        text22 = MathTex(r"\textrm {Basis: }",r"\vec e_1",",",r"\vec e_2",",...,",r"\vec e_i").next_to(text21,DOWN*1.2).scale(1.5)
        text23 = MathTex(r"\vec v","=","v^1",r"\vec e_1","+","v^2",r"\vec e_2","+...+","v^i",r"\vec e_i}").next_to(text22,DOWN).scale(1.5)

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

        text24 = MathTex(r"\textrm{The orthonormal basis in } \mathbb{R}^2 \textrm{ is:}").move_to(UP).scale(1.3)
        text25 = MathTex(r"\vec e_x",",",r"\vec e_y").next_to(text24,DOWN).scale(1.5)
        text25[0].set_color(color=GREEN)
        text25[2].set_color(color=GREEN)

        vcomp = MathTex("1",r"\vec e_x","+","2",r"\vec e_y")
        vcomp[0].set_color(color=BLUE)
        vcomp[1].set_color(color=GREEN)
        vcomp[3].set_color(color=BLUE)
        vcomp[4].set_color(color=GREEN)

        grid=NumberPlane().set_color(color="#878787")

        ex = Arrow([0,0,0],[1,0,0],color=GREEN,buff=0)
        ey = Arrow([0,0,0],[0,1,0],color=GREEN,buff=0)
        exlabel = MathTex(r"\vec e_x").set_color(color=GREEN).next_to(ex,DOWN)
        eylabel = MathTex(r"\vec e_y").set_color(color=GREEN).next_to(ey,LEFT)

        self.play(Write(text24),Write(text25))
        self.wait(4)
        self.play(FadeOut(text24),FadeOut(text25))
        self.play(ShowCreation(grid),ShowCreation(ex),ShowCreation(ey),Write(exlabel),Write(eylabel))
        self.wait(4)
        self.play(FadeOut(exlabel),FadeOut(eylabel))

        v = Arrow([0,0,0],[1,2,0],color=BLUE,buff=0)
        vtext=MathTex(r"\vec v","=").move_to([-3,2,0])
        vtext[0].set_color(color=BLUE)
        vm = Matrix([[1],[2]],left_bracket="\\big(",right_bracket="\\big)").next_to(vtext,RIGHT).set_color(BLUE)
        vex = ex.copy()
        vey = Arrow([1,0,0],[1,2,0],color=GREEN,buff=0)
        vxb = Brace(vex)
        vyb = Brace(vey,RIGHT)
        vxlabel = vxb.get_tex("1",r"\vec e_x")
        vylabel = vyb.get_tex("2",r"\vec e_y")
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
        v2xlabel = v2xb.get_tex("3",r"\vec e_x")
        v2ylabel = v2yb.get_tex("-3",r"\vec e_y")
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
        v3xlabel = v3xb.get_tex("4",r"\vec e_x")
        v3ylabel = v3yb.get_tex("3",r"\vec e_y")
        v3xlabel[0].set_color(color=BLUE)
        v3xlabel[1].set_color(color=GREEN)
        v3ylabel[0].set_color(color=BLUE)
        v3ylabel[1].set_color(color=GREEN)

        self.play(GrowFromCenter(v),Transform(ey,vey),ShowCreation(vxb),
                  ShowCreation(vyb),Write(vxlabel),Write(vylabel),Write(vtext),Write(vm))
        self.wait(4)
        self.play(Transform(v,v2),Transform(ex,v2ex),Transform(ey,v2ey),Transform(vxb,v2xb),
                  Transform(vyb,v2yb),Transform(vxlabel,v2xlabel),Transform(vylabel,v2ylabel),
                  Transform(vm,v2m),Transform(vtext,v2text))
        self.wait(4)
        self.play(Transform(v,v3),Transform(ex,v3ex),Transform(ey,v3ey),Transform(vxb,v3xb),
                  Transform(vyb,v3yb),Transform(vxlabel,v3xlabel),Transform(vylabel,v3ylabel),
                  Transform(vm,v3m),Transform(vtext,v3text))
        self.wait(4)
        self.play(Transform(ex,Arrow([0,0,0],[1,0,0],color=GREEN,buff=0)),Transform(ey,Arrow([0,0,0],[0,1,0],color=GREEN,buff=0)),FadeOut(vxb),FadeOut(vyb),FadeOut(vxlabel),FadeOut(vylabel),
                  FadeOut(vm),FadeOut(vtext),Write(exlabel),Write(eylabel))
        self.wait(4)

        e2x = Arrow([0,0,0],[2,0,0],color=RED,buff=0)
        e2y = Arrow([0,0,0],[0,2,0],color=RED,buff=0)
        v4x = Arrow([0,0,0],[4,0,0],color=RED,buff=0)
        v4y = Arrow([4,0,0],[4,3,0],color=RED,buff=0)
        v4text=MathTex(r"\vec v","=").move_to(LEFT*3 +UP*2)
        v4text[0].set_color(color=BLUE)
        v4m = Matrix([[2],[1.5]],left_bracket="\\big(",right_bracket="\\big)").next_to(vtext,RIGHT).set_color(BLUE)
        v4xb = Brace(v4x,DOWN)
        v4yb = Brace(v4y,RIGHT)
        v4xblabel = v4xb.get_tex("2",r"\bar e_x")
        v4yblabel = v4yb.get_tex(r"\frac{3}{2}",r"\bar e_y")
        v4xblabel[1].set_color(color=RED)
        v4yblabel[1].set_color(color=RED)
        e2xlabel = MathTex(r"\bar e_x").set_color(color=RED).next_to(e2x,DOWN)
        e2ylabel = MathTex(r"\bar e_y").set_color(color=RED).next_to(e2y,RIGHT)
        text26 = MathTex(r"\bar e_x","=2",r"\vec e_x").move_to([-3,0,0])
        text27 = MathTex(r"\bar e_y","=2",r"\vec e_y").next_to(text26,DOWN)
        text26[0].set_color(color=RED)
        text26[2].set_color(color=GREEN)
        text27[0].set_color(color=RED)
        text27[2].set_color(color=GREEN)


        grid2 = NumberPlane(x_line_frequency=2,y_line_frequency=2).set_color(color="#878787")
        self.play(Transform(grid,grid2),Transform(ex,e2x),Transform(ey,e2y),Transform(exlabel,e2xlabel),Transform(eylabel,e2ylabel),
                  Write(text26),Write(text27))
        self.wait(4)
        self.play(Write(v4text),Write(v4m),Transform(ex,v4x),Transform(ey,v4y),ShowCreation(v4xb),ShowCreation(v4yb),Transform(exlabel,v4xblabel),Transform(eylabel,v4yblabel))
        self.wait(4)
        self.play(FadeOut(v),FadeOut(v4text),FadeOut(grid),FadeOut(v4m),FadeOut(ex),FadeOut(ey),FadeOut(v4xb),FadeOut(v4yb),FadeOut(exlabel),FadeOut(eylabel),FadeOut(text26),FadeOut(text27))

        text28 = Text("Vector components are contravariant.").move_to(UP*2.5)
        text29 = Text("They transform opposite to the basis").next_to(text28,DOWN)
        text30 = Text("under a change of basis.").next_to(text29,DOWN)
        text31 = Text("Contravariant components are denoted").next_to(text30,DOWN)
        text32 = Text("with superscripts").next_to(text31,DOWN)

        self.play(Write(text28),Write(text29),Write(text30),Write(text31),Write(text32))
        self.wait(5)
        self.play(FadeOut(text28),FadeOut(text29),FadeOut(text30),FadeOut(text31),FadeOut(text32))

        text33 = Text("If we double our basis vectors,").move_to(UP*2.5)
        text34 = Text("we halve our vector components").next_to(text33,DOWN)
        text35 = MathTex(r"\bar e_x","=2",r"\vec e_x",r"\quad",r"\bar e_y","=2",r"\vec e_y").next_to(text34,DOWN*2).scale(2)
        text35[0].set_color(color=RED)
        text35[2].set_color(color=GREEN)
        text35[4].set_color(color=RED)
        text35[6].set_color(color=GREEN)
        text37 = MathTex(r"\vec v","=2",r"\vec e_x","+2",r"\vec e_y").next_to(text35,DOWN*2).scale(2)
        text38 = MathTex(r"\vec v",r"=1",r"\bar e_x",r"+1",r"\bar e_y").next_to(text37,DOWN*2).scale(2)
        text37[0].set_color(color=BLUE)
        text37[2].set_color(color=GREEN)
        text37[4].set_color(color=GREEN)
        text38[0].set_color(color=BLUE)
        text38[2].set_color(color=RED)
        text38[4].set_color(color=RED)

        self.play(Write(text33),Write(text34),Write(text35),Write(text37),Write(text38))
        self.wait(4)
        self.play(FadeOut(text33),FadeOut(text34),FadeOut(text35),FadeOut(text37),FadeOut(text38))
        self.wait()

class Scene3 (Scene):
    def construct(self):
        text1 = Text("Now we are ready to talk about covectors!")

        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))

        text2 = Text("Our vectors lived in our vector space V,").move_to(UP*1.5)
        text3 = Text("and covectors live in the dual space V*.").next_to(text2,DOWN)
        text4 = Text("We will write them with greek letters.").next_to(text3,DOWN)

        self.play(Write(text2),Write(text3),Write(text4))
        self.wait(5)
        self.play(FadeOut(text2),FadeOut(text3),FadeOut(text4))

        text5 = Text("Covectors are linear functionals.").move_to(UP*2.2)
        text6 = Text("They map vectors to the real numbers.").next_to(text5,DOWN*1.5)
        text7 = MathTex(r"\alpha: V \rightarrow \mathbb{R}").next_to(text6,DOWN*1.5).scale(2)
        text8 = MathTex(r"\alpha","(",r"\vec v",")","=x").next_to(text7,DOWN).scale(2)
        text8[0].set_color(color=YELLOW)
        text8[2].set_color(color=BLUE)

        self.play(Write(text5),Write(text6),Write(text7),Write(text8))
        self.wait(5)
        self.play(FadeOut(text5),FadeOut(text6),FadeOut(text7),FadeOut(text8))

        text9 = Text("Because V* is also a vector space,").move_to(UP*1.5)
        text10 = Text("Covectors have many of the same").next_to(text9,DOWN)
        text11 = Text( "properties as vectors.").next_to(text10,DOWN)

        self.play(Write(text9),Write(text10),Write(text11))
        self.wait(5)
        self.play(FadeOut(text9),FadeOut(text10),FadeOut(text11))

        text12 = Text("We have a notion of adding Covectors,").move_to(UP*1.5)
        text13 = MathTex(r"\alpha","(",r"\vec v",")+",r"\beta","(",r"\vec v",")=",r"\gamma","(",r"\vec v",")").scale(2).next_to(text12,DOWN)
        text14 = Text("And multiplication by a scalar").next_to(text13,DOWN)
        text15 = MathTex("n",r"\alpha","(",r"\vec v",")=nx").scale(2).next_to(text14,DOWN)
        text13[0].set_color(color=YELLOW)
        text13[2].set_color(color=BLUE)
        text13[4].set_color(color=ORANGE)
        text13[6].set_color(color=BLUE)
        text13[8].set_color(color=RED)
        text13[10].set_color(color=BLUE)
        text15[1].set_color(color=YELLOW)
        text15[3].set_color(color=BLUE)

        self.play(Write(text12),Write(text13),Write(text14),Write(text15))
        self.wait(5)
        self.play(FadeOut(text12),FadeOut(text13),FadeOut(text14),FadeOut(text15))

        text15 = Text("By linear we mean that").move_to(UP*1.5)
        text16 = Text("multiplication distributes over addition").next_to(text15,DOWN)
        text17 = MathTex("n(",r"\alpha","(",r"\vec v",")+",r"\beta","(",r"\vec v","))=n",r"\gamma","(",r"\vec v",")").scale(2).next_to(text16,DOWN)
        text18 = MathTex("n",r"\alpha","(",r"\vec v",")+n",r"\beta","(",r"\vec v",")=n",r"\gamma","(",r"\vec v",")").scale(2).next_to(text16,DOWN)
        text17[1].set_color(color=YELLOW)
        text17[3].set_color(color=BLUE)
        text17[5].set_color(color=ORANGE)
        text17[7].set_color(color=BLUE)
        text17[9].set_color(color=RED)
        text17[11].set_color(color=BLUE)
        text18[1].set_color(color=YELLOW)
        text18[3].set_color(color=BLUE)
        text18[5].set_color(color=ORANGE)
        text18[7].set_color(color=BLUE)
        text18[9].set_color(color=RED)
        text18[11].set_color(color=BLUE)

        self.play(Write(text15),Write(text16),Write(text17))
        self.wait(2)
        self.play(Transform(text17,text18))
        self.wait(3)

        text19 = Text("and that we can move multiplication").move_to(UP*1.5)
        text20 = Text("in and out of the covector").next_to(text19,DOWN)
        text21 = MathTex(r"\alpha","(n",r"\vec v",")+",r"\beta","(n",r"\vec v",")=",r"\gamma","(n",r"\vec v",")").scale(2).next_to(text20,DOWN)
        text21[0].set_color(color=YELLOW)
        text21[2].set_color(color=BLUE)
        text21[4].set_color(color=ORANGE)
        text21[6].set_color(color=BLUE)
        text21[8].set_color(color=RED)
        text21[10].set_color(color=BLUE)
        text22 = MathTex("(",r"\alpha","+",r"\beta",")","(n",r"\vec v",")=",r"\gamma","(n",r"\vec v",")").scale(2).next_to(text20,DOWN)
        text22[1].set_color(color=YELLOW)
        text22[3].set_color(color=ORANGE)
        text22[6].set_color(color=BLUE)
        text22[8].set_color(color=RED)
        text22[10].set_color(color=BLUE)
        text23 = Text("and also distribute over vector addition").move_to(UP*1.5)
        alpha1 = MathTex(r"\alpha","(",r"\vec v",")=",r"\alpha","(",r"\vec u",")+",r"\alpha","(",r"\vec w",")").next_to(text20,DOWN).scale(2)
        alpha2 = MathTex(r"\alpha","(",r"\vec v",")=",r"\alpha","(",r"\vec u","+",r"\vec w",")").next_to(text20,DOWN).scale(2)
        alpha1[0].set_color(color=YELLOW)
        alpha1[2].set_color(color=BLUE)
        alpha1[4].set_color(color=YELLOW)
        alpha1[6].set_color(color=PURPLE)
        alpha1[8].set_color(color=YELLOW)
        alpha1[10].set_color(color=PINK)
        alpha2[0].set_color(color=YELLOW)
        alpha2[2].set_color(color=BLUE)
        alpha2[4].set_color(color=YELLOW)
        alpha2[6].set_color(color=PURPLE)
        alpha2[8].set_color(color=PINK)
        where = MathTex("*",r"\vec v","=",r"\vec u","+",r"\vec w").next_to(alpha1,DOWN).scale(1.5)
        where[1].set_color(color=BLUE)
        where[3].set_color(color=PURPLE)
        where[5].set_color(color=PINK)

        self.play(Transform(text15,text19), Transform(text16,text20))
        self.wait()
        self.play(Transform(text17,text21))
        self.wait(3)
        self.play(Transform(text17,text22))
        self.wait(2)
        self.play(FadeOut(text16),Transform(text15,text23),Transform(text17,alpha2),Write(where))
        self.wait(3)
        self.play(Transform(text17,alpha1),)
        self.wait(3)
        self.play(FadeOut(where),FadeOut(text17),FadeOut(text15))
        self.wait()

        text24 = Text("Using linearity we can see how a covector").move_to(UP*2)
        text25 = Text("acts on a vector by seeing how it acts").next_to(text24,DOWN)
        text26 = Text("on the basis vectors").next_to(text25,DOWN)

        alpha3 = MathTex(r"\alpha","(",r"\vec v",")=",r"\alpha","(","v^x",r"\vec e_x","+","v^y",r"\vec e_y",")\quad").next_to(text26,DOWN*2).scale(2)
        alpha3[0].set_color(color=YELLOW)
        alpha3[2].set_color(color=BLUE)
        alpha3[4].set_color(color=YELLOW)
        alpha3[6].set_color(color=BLUE)
        alpha3[7].set_color(color=GREEN)
        alpha3[9].set_color(color=BLUE)
        alpha3[10].set_color(color=GREEN)

        alpha4 = MathTex(r"\alpha","(",r"\vec v",")=",r"\alpha","(","v^x",r"\vec e_x",")+",r"\alpha","(","v^y",r"\vec e_y",")").next_to(text26,DOWN*2).scale(2)
        alpha4[0].set_color(color=YELLOW)
        alpha4[2].set_color(color=BLUE)
        alpha4[4].set_color(color=YELLOW)
        alpha4[6].set_color(color=BLUE)
        alpha4[7].set_color(color=GREEN)
        alpha4[9].set_color(color=YELLOW)
        alpha4[11].set_color(color=BLUE)
        alpha4[12].set_color(color=GREEN)

        alpha5 = MathTex(r"\alpha","(",r"\vec v",")=","v^x",r"\alpha","(",r"\vec e_x",")+","v^y",r"\alpha","(",r"\vec e_y",")").next_to(text26,DOWN*2).scale(2)
        alpha5[0].set_color(color=YELLOW)
        alpha5[2].set_color(color=BLUE)
        alpha5[4].set_color(color=BLUE)
        alpha5[5].set_color(color=YELLOW)
        alpha5[7].set_color(color=GREEN)
        alpha5[9].set_color(color=BLUE)
        alpha5[10].set_color(color=YELLOW)
        alpha5[12].set_color(color=GREEN)

        self.play(Write(text24),Write(text25),Write(text26),Write(alpha3))
        self.wait(6)
        self.play(Transform(alpha3,alpha4))
        self.wait(5)
        self.play(Transform(alpha3,alpha5))
        self.wait(5)
        self.play(FadeOut(text24),FadeOut(text25),FadeOut(text26),FadeOut(alpha3))
        self.wait()

        text27 = Text("We can interpret covectors geometrically")
        text28 = Text("While we thought of vectors as arrows,").move_to(UP*2)
        text29 = Text("we will think of covectors as oriented").next_to(text28,DOWN)
        text30 = Text("stacks of hyperplanes in our space").next_to(text29,DOWN)
        text31 = Text("In 2 dimensions these are just lines").next_to(text30,DOWN)

        self.play(Write(text27))
        self.wait(2)
        self.play(FadeOut(text27))
        self.play(Write(text28),Write(text29),Write(text30),Write(text31))
        self.wait(4)
        self.play(FadeOut(text28),FadeOut(text29),FadeOut(text30),FadeOut(text31))

        line1 = Line([-5,5,0],[5,-5,0]).set_color(color=GREY).set_opacity(0.5)
        arrow1 = Arrow([0,0,0],[0.3,0.3,0],buff=0).set_color(color=GREY).set_opacity(0.5)
        stack1 = VGroup(line1,arrow1)
        stack2 = stack1.copy().move_to([1,1,0])
        stack3 = stack1.copy().move_to([2,2,0])
        stack4 = stack1.copy().move_to([3,3,0])
        stack5 = stack1.copy().move_to([4,4,0])
        stack6 = stack1.copy().move_to([5,5,0])
        stack7 = stack1.copy().move_to([-1,-1,0])
        stack8 = stack1.copy().move_to([-2,-2,0])
        stack9 = stack1.copy().move_to([-3,-3,0])
        stack10 = stack1.copy().move_to([-4,-4,0])
        stack11 = stack1.copy().move_to([-5,-5,0])

        alpha = VGroup(stack1.set_color(color=WHITE),stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9,stack10,stack11).move_to([-1,0,0])

        v = Arrow([-1,0,0],[3,2,0],buff=0,color=BLUE)
        vx = Arrow([-1,0,0],[3,0,0],buff=0,color=GREEN)
        vy = Arrow([3,0,0],[3,2,0],buff=0,color=GREEN)

        b1 = BraceBetweenPoints([3,2,0],[-1,0,0])
        b1text = b1.get_tex(r"\alpha","(",r"\vec v",")=3")
        b1text[0].set_color(color=YELLOW)
        b1text[2].set_color(color=BLUE)
        sidenote1 = MathTex(r"\textrm{The value of }", r"\alpha","(",r"\vec v",")",r"\textrm{ is the number}").move_to([0,-1.5,0]).scale(1.5)
        sidenote1[1].set_color(color=YELLOW)
        sidenote1[3].set_color(color=BLUE)
        sidenote2 = MathTex(r"\textrm{of stacks }",r"\vec v", r"\textrm{ crosses in their direction}").scale(1.5).next_to(sidenote1,DOWN)
        sidenote2[1].set_color(color=BLUE)


        self.play(ShowCreation(alpha))
        self.wait(2)
        self.play(GrowFromCenter(v),GrowFromCenter(b1),Write(b1text),Write(sidenote1),Write(sidenote2))
        self.wait(4)

        b2= Brace(vx,direction=DOWN)
        b3= Brace(vy,direction=RIGHT)
        b2text = b2.get_tex("2",r"\alpha","(",r"\vec e_x",")=2")
        b2text[0].set_color(color=BLUE)
        b2text[1].set_color(color=YELLOW)
        b2text[3].set_color(color=GREEN)
        b3text = b3.get_tex("1",r"\alpha","(",r"\vec e_y",")=1")
        b3text[0].set_color(color=BLUE)
        b3text[1].set_color(color=YELLOW)
        b3text[3].set_color(color=GREEN)
        componentnote1 = Text("As previously stated we can look at").move_to([0,-2,0])
        componentnote2 = Text("the covector's action on the basis").next_to(componentnote1,DOWN)

        v2 = Arrow([-1,0,0],[-5,-2,0],buff=0,color=BLUE)
        b4 = BraceBetweenPoints([-1,0,0],[-5,-2,0])
        b4text = b4.get_tex(r"\quad\alpha","(",r"-\vec v",")=-3")
        b4text[0].set_color(color=YELLOW)
        b4text[2].set_color(color=BLUE)
        sidenote3 = Text("Crossing stacks in the opposite direction").move_to([0,2,0])
        sidenote4 = Text("gives us negative values").next_to(sidenote3,DOWN)

        self.play(Write(componentnote1),Write(componentnote2),FadeOut(sidenote1),FadeOut(sidenote2),FadeOut(b1),FadeOut(b1text), ShowCreation(vx),ShowCreation(vy),ShowCreation(b2),ShowCreation(b3),ShowCreation(b2text),ShowCreation(b3text))
        self.wait(5)
        self.play(FadeOut(componentnote1),FadeOut(componentnote2),FadeOut(vx),FadeOut(vy),FadeOut(b2),FadeOut(b3),FadeOut(b2text),FadeOut(b3text),Transform(v,v2))
        self.play(ShowCreation(b4),Write(b4text),Write(sidenote3),Write(sidenote4))
        self.wait(4)
        self.play(FadeOut(v),FadeOut(b4),FadeOut(b4text),Uncreate(alpha),FadeOut(sidenote3),FadeOut(sidenote4))
        self.wait()

        text32 = Text("Multiplying a covector by a scalar").move_to(UP*1.5)
        text34 = Text("changes the density of the hyperplanes.").next_to(text32,DOWN)

        self.play(Write(text32),Write(text34))
        self.wait(3)
        self.play(FadeOut(text32),FadeOut(text34))

        text35 = Text("This lines up with our notion of linearity").move_to(UP*2)
        text36 = Text("as we can scale the covector and cross").next_to(text35,DOWN)
        text37 = Text("more stacks with the same vector.").next_to(text36,DOWN)
        text38 = MathTex("n",r"\alpha","(",r"\vec v",")").next_to(text37,DOWN).scale(2)
        text38[1].set_color(color=YELLOW)
        text38[3].set_color(color=BLUE)

        self.play(Write(text35),Write(text36),Write(text37),Write(text38))
        self.wait(5)

        text40 = Text("Or scale the vector and cross more").move_to(UP*2)
        text41 = Text("stacks on the original covector").next_to(text40,DOWN)
        text42 = MathTex(r"\alpha","(n",r"\vec v",")").next_to(text37,DOWN).scale(2)
        text42[0].set_color(color=YELLOW)
        text42[2].set_color(color=BLUE)

        self.play(Transform(text35,text40),Transform(text36,text41),FadeOut(text37),Transform(text38,text42))
        self.wait(5)
        self.play(FadeOut(text35),FadeOut(text36),FadeOut(text38))

class Scene4(Scene):
    def construct(self):
        u = Arrow([-1,0,0],[1,2,0],buff=0).set_color(color=BLUE)
        w = Arrow([-1,0,0],[3,4,0],buff=0).set_color(color=BLUE)
        bu = BraceBetweenPoints([-1,0,0],[1,2,0])
        bw = BraceBetweenPoints([-1,0,0],[3,4,0])
        wtext1 = bu.get_tex(r"\alpha","(",r"\vec v",")=2")
        wtext1[0].set_color(color=YELLOW)
        wtext1[2].set_color(color=BLUE)
        wtext2 = bw.get_tex(r"\alpha","(2",r"\vec v",")=4")
        wtext2[0].set_color(color=YELLOW)
        wtext2[2].set_color(color=BLUE)
        wtext3 = bu.get_tex("2",r"\alpha","(",r"\vec v",")=4")
        wtext3[1].set_color(color=YELLOW)
        wtext3[3].set_color(color=BLUE)

        line1 = Line([-5,5,0],[5,-5,0]).set_color(color=GREY).set_opacity(0.5)
        arrow1 = Arrow([0,0,0],[0.3,0.3,0],buff=0).set_color(color=GREY).set_opacity(0.5)
        stack1 = VGroup(line1,arrow1)
        stack2 = stack1.copy().move_to([1,1,0])
        stack3 = stack1.copy().move_to([2,2,0])
        stack4 = stack1.copy().move_to([3,3,0])
        stack5 = stack1.copy().move_to([4,4,0])
        stack6 = stack1.copy().move_to([5,5,0])
        stack7 = stack1.copy().move_to([-1,-1,0])
        stack8 = stack1.copy().move_to([-2,-2,0])
        stack9 = stack1.copy().move_to([-3,-3,0])
        stack10 = stack1.copy().move_to([-4,-4,0])
        stack11 = stack1.copy().move_to([-5,-5,0])

        alpha = VGroup(stack1.set_color(color=WHITE),stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9,stack10,stack11).move_to([-1,0,0])

        beta = VGroup(stack1.set_color(color=WHITE),
                      stack1.copy().move_to([-5,-5,0]),
                      stack1.copy().move_to([-4.5,-4.5,0]),
                      stack1.copy().move_to([-4,-4,0]),
                      stack1.copy().move_to([-3.5,-3.5,0]),
                      stack1.copy().move_to([-3,-3,0]),
                      stack1.copy().move_to([-2.5,-2.5,0]),
                      stack1.copy().move_to([-2,-2,0]),
                      stack1.copy().move_to([-1.5,-1.5,0]),
                      stack1.copy().move_to([-1,-1,0]),
                      stack1.copy().move_to([-0.5,-0.5,0]),
                      stack1.copy().move_to([5,5,0]),
                      stack1.copy().move_to([4.5,4.5,0]),
                      stack1.copy().move_to([4,4,0]),
                      stack1.copy().move_to([3.5,3.5,0]),
                      stack1.copy().move_to([3,3,0]),
                      stack1.copy().move_to([2.5,2.5,0]),
                      stack1.copy().move_to([2,2,0]),
                      stack1.copy().move_to([0.5,0.5,0]),
                      stack1.copy().move_to([1,1,0]),
                      stack1.copy().move_to([1.5,1.5,0]),
                      stack1.copy().move_to([0,0,0]))

        self.play(ShowCreation(alpha),ShowCreation(u),ShowCreation(bu),ShowCreation(wtext1))
        self.wait(4)
        self.play(Transform(u,w),Transform(bu,bw),Transform(wtext1,wtext2))
        self.wait(4)
        self.play(Transform(alpha,beta), Transform(u,Arrow([-1,0,0],[1,2,0],buff=0).set_color(color=BLUE)),Transform(wtext1,wtext3),Transform(bu,BraceBetweenPoints([-1,0,0],[1,2,0])))
        self.wait(4)
        self.play(FadeOut(alpha),FadeOut(u),FadeOut(bu),FadeOut(wtext1))
        self.wait()

        text43 = Text("Covectors can also have a basis.").move_to(UP)
        text44 = MathTex(r"\textrm{Basis covectors in V*: }", r"\epsilon^1",",",r"\epsilon^2",",...,",r"\epsilon^i").scale(1.5).next_to(text43,DOWN)
        text44[1].set_color(color=RED)
        text44[3].set_color(color=RED)
        text44[5].set_color(color=RED)

        self.play(Write(text43),Write(text44))
        self.wait(3)
        self.play(FadeOut(text43),FadeOut(text44))

        text45 = Text("And be written as a linear combination").move_to(UP*1.5)
        text46 = Text("of components and basis covectors").next_to(text45,DOWN)
        text47 = MathTex(r"\alpha","(",r"\vec v",")=",r"\alpha_1",r"\epsilon^1","(",r"\vec v",")+",r"\alpha_2",r"\epsilon^2","(",r"\vec v",")+...+",r"\alpha_i",r"\epsilon^i","(",r"\vec v",")").scale(1.5).next_to(text46,DOWN)
        text47[0].set_color(color=YELLOW)
        text47[2].set_color(color=BLUE)
        text47[4].set_color(color=YELLOW)
        text47[5].set_color(color=RED)
        text47[7].set_color(color=BLUE)
        text47[9].set_color(color=YELLOW)
        text47[10].set_color(color=RED)
        text47[12].set_color(color=BLUE)
        text47[14].set_color(color=YELLOW)
        text47[15].set_color(color=RED)
        text47[17].set_color(color=BLUE)

        self.play(Write(text45),Write(text46),Write(text47))
        self.wait(5)
        self.play(FadeOut(text45),FadeOut(text46),FadeOut(text47))

        text48 = Text("The basis covectors can be understood").move_to(UP*2)
        text49 = Text("by their action on the basis vectors").next_to(text48,DOWN)
        text50 = MathTex(r"\epsilon^1","(",r"\vec e_1",")=1\quad",r"\epsilon^1","(",r"\vec e_2",")=0").scale(2).next_to(text49,DOWN)
        text51 = MathTex(r"\epsilon^2","(",r"\vec e_1",")=0\quad",r"\epsilon^2","(",r"\vec e_2",")=1").scale(2).next_to(text50,DOWN)
        text50[0].set_color(color=RED)
        text50[2].set_color(color=GREEN)
        text50[4].set_color(color=RED)
        text50[6].set_color(color=GREEN)
        text51[0].set_color(color=RED)
        text51[2].set_color(color=GREEN)
        text51[4].set_color(color=RED)
        text51[6].set_color(color=GREEN)

        self.play(Write(text48),Write(text49),Write(text50),Write(text51))
        self.wait(5)
        self.play(FadeOut(text48),FadeOut(text49),FadeOut(text50),FadeOut(text51))

        text52 = Text("They can also be viewed geometrically").move_to(UP)
        text53 = Text("In the same fashion as covectors").next_to(text52,DOWN)

        self.play(Write(text52),Write(text53))
        self.wait(3)
        self.play(FadeOut(text52),FadeOut(text53))

        linee1 = Line([0,-4,0],[0,4,0]).set_color(color=GREY).set_opacity(0.5)
        arrowe1 = Arrow([0,0,0],[0.4,0,0],buff=0).set_color(color=GREY).set_opacity(0.5)
        stacke1 = VGroup(linee1,arrowe1)
        e1 = VGroup(stacke1.copy().move_to([-7,0,0]),stacke1.copy().move_to([-6,0,0]),stacke1.copy().move_to([-5,0,0]),stacke1.copy().move_to([-4,0,0]),stacke1.copy().move_to([-3,0,0]),
              stacke1.copy().move_to([-2,0,0]),stacke1.copy().move_to([-1,0,0]),stacke1.copy().set_color(color=WHITE).move_to([0,0,0]),stacke1.copy().move_to([1,0,0]),stacke1.copy().move_to([2,0,0]),
              stacke1.copy().move_to([3,0,0]),stacke1.copy().move_to([4,0,0]),stacke1.copy().move_to([5,0,0]),stacke1.copy().move_to([6,0,0]),stacke1.copy().move_to([7,0,0])).move_to([0.2,0,0])
        linee2 = Line([-8,0,0],[8,0,0]).set_color(color=GREY).set_opacity(0.5)
        arrowe2 = Arrow([0,0,0],[0,0.4,0],buff=0).set_color(color=GREY).set_opacity(0.5)
        stacke2 = VGroup(linee2,arrowe2)
        e2 = VGroup(stacke2.copy().move_to([0,-4,0]),stacke2.copy().move_to([0,-3,0]),stacke2.copy().move_to([0,-2,0]),stacke2.copy().move_to([0,-1,0]), stacke2.copy().set_color(color=WHITE).move_to([0,0,0]),
                    stacke2.copy().move_to([0,1,0]),stacke2.copy().move_to([0,2,0]),stacke2.copy().move_to([0,3,0]),stacke2.copy().move_to([0,4,0])).move_to([0,0.2,0])
        ex = Arrow([0,0,0],[1,0,0],buff=0,color=GREEN)
        ey = Arrow([0,0,0],[0,1,0],buff=0,color=GREEN)
        ex1 = Arrow([0,0,0],[1,0,0],buff=0,color=GREEN)
        ey1 = Arrow([0,0,0],[0,1,0],buff=0,color=GREEN)

        e1text = MathTex("\epsilon^x").set_color(color=RED).move_to([-1,1,0]).scale(2)
        e2text = MathTex("\epsilon^y").set_color(color=RED).move_to([-1,1,0]).scale(2)

        exb = Brace(ex,direction=DOWN)
        eyb = Brace(ey,direction=RIGHT)
        ex1b = Brace(ex,direction=DOWN)
        ey1b = Brace(ey,direction=RIGHT)
        exb1text = exb.get_tex(r"\epsilon^x","(",r"\vec e_x",")=1")
        exb1text[0].set_color(color=RED)
        exb1text[2].set_color(color=GREEN)
        exb2text = eyb.get_tex(r"\epsilon^x","(",r"\vec e_y",")=0")
        exb2text[0].set_color(color=RED)
        exb2text[2].set_color(color=GREEN)
        eyb1text = eyb.get_tex(r"\epsilon^y","(",r"\vec e_y",")=1")
        eyb1text[0].set_color(color=RED)
        eyb1text[2].set_color(color=GREEN)
        eyb2text = exb.get_tex(r"\epsilon^y","(",r"\vec e_x",")=0")
        eyb2text[0].set_color(color=RED)
        eyb2text[2].set_color(color=GREEN)

        self.play(ShowCreation(e1),Write(e1text),ShowCreation(ex))
        self.play(GrowFromCenter(exb),Write(exb1text))
        self.wait(3)
        self.play(Transform(ex,ey),Transform(exb1text,exb2text),Transform(exb,eyb))
        self.wait(3)
        self.play(Transform(e1,e2),Transform(exb1text,eyb1text),Transform(e1text,e2text))
        self.wait(3)
        self.play(Transform(ex,ex1),Transform(exb1text,eyb2text),Transform(exb,ex1b))
        self.wait(3)
        self.play(FadeOut(e1),FadeOut(ex),FadeOut(e1text),FadeOut(exb),FadeOut(exb1text))

        text54 = Text("Covectors are so called because their").move_to(UP*2).scale(0.9)
        text55 = Text("components co-vary with a change of").next_to(text54,DOWN).scale(0.9)
        text56 = Text("basis in contrast with vectors whose").next_to(text55,DOWN).scale(0.9)
        text57 = Text("components contra-vary to a change of basis").next_to(text56,DOWN).scale(0.9)

        self.play(Write(text54),Write(text55),Write(text56),Write(text57))
        self.wait(5)
        self.play(FadeOut(text54),FadeOut(text55),FadeOut(text56),FadeOut(text57))

        text58 = Text("A side note about stack spacing")

        self.play(Write(text58))
        self.wait(2)
        self.play(FadeOut(text58))

        text59 = Text("We have arbitrarily chosen to space").move_to(UP*2)
        text60 = Text("the stacks at integer sets, and").next_to(text59,DOWN)
        text61 = Text("applying the covector adds 1 for each").next_to(text60,DOWN)
        text62 = Text("stack the vector pierces.").next_to(text61,DOWN)

        self.play(Write(text59),Write(text60),Write(text61),Write(text62))
        self.wait(6)
        self.play(FadeOut(text59),FadeOut(text60),FadeOut(text61),FadeOut(text62))

        text63 = Text("We could have also drawn them twice").move_to(UP)
        text64 = Text("as dense and added 1/2 for each stack.").next_to(text63,DOWN)

        self.play(Write(text63),Write(text64))
        self.wait(4)
        self.play(FadeOut(text63),FadeOut(text64))

        a = Arrow([-1,0,0],[1.5,2.5,0],buff=0,color=BLUE)
        b5 = BraceBetweenPoints([-1,0,0],[1.5,2.5,0])
        b5text = b5.get_tex(r"\alpha","(",r"\vec v",")=2.5")
        b5text[0].set_color(color=YELLOW)
        b5text[2].set_color(color=BLUE)

        line1 = Line([-5,5,0],[5,-5,0]).set_color(color=GREY).set_opacity(0.5)
        arrow1 = Arrow([0,0,0],[0.3,0.3,0],buff=0).set_color(color=GREY).set_opacity(0.5)
        stack1 = VGroup(line1,arrow1)
        stack2 = stack1.copy().move_to([1,1,0])
        stack3 = stack1.copy().move_to([2,2,0])
        stack4 = stack1.copy().move_to([3,3,0])
        stack5 = stack1.copy().move_to([4,4,0])
        stack6 = stack1.copy().move_to([5,5,0])
        stack7 = stack1.copy().move_to([-1,-1,0])
        stack8 = stack1.copy().move_to([-2,-2,0])
        stack9 = stack1.copy().move_to([-3,-3,0])
        stack10 = stack1.copy().move_to([-4,-4,0])
        stack11 = stack1.copy().move_to([-5,-5,0])

        alpha1 = VGroup(stack1.set_color(color=WHITE),stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9,stack10,stack11).move_to([-1,0,0])

        beta1 = VGroup(stack1.set_color(color=WHITE),
                      stack1.copy().move_to([-5,-5,0]),
                      stack1.copy().move_to([-4.5,-4.5,0]),
                      stack1.copy().move_to([-4,-4,0]),
                      stack1.copy().move_to([-3.5,-3.5,0]),
                      stack1.copy().move_to([-3,-3,0]),
                      stack1.copy().move_to([-2.5,-2.5,0]),
                      stack1.copy().move_to([-2,-2,0]),
                      stack1.copy().move_to([-1.5,-1.5,0]),
                      stack1.copy().move_to([-1,-1,0]),
                      stack1.copy().move_to([-0.5,-0.5,0]),
                      stack1.copy().move_to([5,5,0]),
                      stack1.copy().move_to([4.5,4.5,0]),
                      stack1.copy().move_to([4,4,0]),
                      stack1.copy().move_to([3.5,3.5,0]),
                      stack1.copy().move_to([3,3,0]),
                      stack1.copy().move_to([2.5,2.5,0]),
                      stack1.copy().move_to([2,2,0]),
                      stack1.copy().move_to([0.5,0.5,0]),
                      stack1.copy().move_to([1,1,0]),
                      stack1.copy().move_to([1.5,1.5,0]),
                      stack1.copy().move_to([0,0,0]))

        self.play(ShowCreation(alpha1),GrowFromCenter(a),GrowFromCenter(b5),Write(b5text))
        self.wait(3)
        self.play(Transform(alpha1,beta1))
        self.wait(3)
        self.play(FadeOut(alpha1),FadeOut(a),FadeOut(b5),FadeOut(b5text))

        text65 = Text("Whats really going on is that the").move_to(UP*1.5)
        text66 = Text("covector stacks are dense with each").next_to(text65,DOWN)
        text67 = Text("stack contributing a small ammount").next_to(text66,DOWN)

        self.play(Write(text65),Write(text66),Write(text67))
        self.wait(5)
        self.play(FadeOut(text65),FadeOut(text66),FadeOut(text67))


class Scene5(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=-1.5,
            x_max=3.5,
            x_axis_width=10,
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
        text1 = Text("To understand the definite integral in").move_to(UP*1.5)
        text2 = Text("terms of covectors we will need to ").next_to(text1,DOWN)
        text3 = Text("reinterpret the d in dx").next_to(text2,DOWN)

        self.play(Write(text1),Write(text2),Write(text3))
        self.wait(5)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))

        text4 = Text("Originally for some variable x,").move_to(UP*1.5)
        text5 = Text("dx is some small nudge").next_to(text4,DOWN)
        text6 = Text("in the x direction.").next_to(text5,DOWN)
        text7 = MathTex(r"x\,\xrightarrow{d}\,dx").scale(1.5).next_to(text6,DOWN)

        self.play(Write(text4),Write(text5),Write(text6),Write(text7))
        self.wait(6)
        self.play(FadeOut(text4),FadeOut(text5),FadeOut(text6),FadeOut(text7))

        text8 = Text("We will now think of d as an operator").move_to(UP*1.5)
        text9 = Text("that takes a scalar field F").next_to(text8,DOWN)
        text10 = Text("and returns a covector field dF").next_to(text9,DOWN)
        text11 = MathTex(r"F\,\xrightarrow{d}\,dF").scale(1.5).next_to(text10,DOWN)

        self.play(Write(text8),Write(text9),Write(text10),Write(text11))
        self.wait(6)
        self.play(FadeOut(text8),FadeOut(text9),FadeOut(text10),FadeOut(text11))

        text12 = Text("A covector field is a map that").move_to(UP*1.5)
        text13 = Text("takes a point in our space and").next_to(text12,DOWN)
        text14 = Text("maps a covector to it").next_to(text13,DOWN)
        text15 = MathTex(r"df: (x_1,x_2,...,x_n)\in\mathbb{R}^n \rightarrow \alpha\in V*").scale(1.5).next_to(text14,DOWN)

        self.play(Write(text12),Write(text13),Write(text14),Write(text15))
        self.wait(7)
        self.play(FadeOut(text12),FadeOut(text13),FadeOut(text14),FadeOut(text15))

        text16 = Text("We can visualize dF as").move_to(UP)
        text17 = Text("the level sets of F ").next_to(text16,DOWN)

        self.play(Write(text16),Write(text17))
        self.wait(3)
        self.play(FadeOut(text16),FadeOut(text17))

        self.setup_axes(animate=True)

        func1 =self.get_graph(lambda x: 4- 2*x,
                                    x_min=-1,
                                    x_max=3).set_color(color=BLUE)
        func2 =self.get_graph(lambda x: 4*x- x**2 +2,
                                    x_min=-1,
                                    x_max=3)
        text18 = MathTex("f(x) = 4-2x").move_to(self.coords_to_point(4.5,3))
        text19 = MathTex("F(x) = 2+4x-x^2").move_to(self.coords_to_point(4.5,3))
        text20 = MathTex("dF").move_to(self.coords_to_point(4.5,-5.5))

        vline1 = self.get_vertical_line_to_graph(-1,func2,DashedLine, color=YELLOW)
        vline2 = self.get_vertical_line_to_graph(2-(math.sqrt(8)),func2,DashedLine, color=YELLOW)
        vline3 = self.get_vertical_line_to_graph(2-(math.sqrt(7)),func2,DashedLine, color=YELLOW)
        vline4 = self.get_vertical_line_to_graph(2-(math.sqrt(6)),func2,DashedLine, color=YELLOW)
        vline5 = self.get_vertical_line_to_graph(2-(math.sqrt(5)),func2,DashedLine, color=YELLOW)
        vline6 = self.get_vertical_line_to_graph(0,func2,DashedLine, color=YELLOW)
        vline7 = self.get_vertical_line_to_graph(2-(math.sqrt(3)),func2,DashedLine, color=YELLOW)
        vline8 = self.get_vertical_line_to_graph(2-(math.sqrt(2)),func2,DashedLine, color=YELLOW)
        vline9 = self.get_vertical_line_to_graph(1,func2,DashedLine, color=YELLOW)
        vline10 = self.get_vertical_line_to_graph(2,func2,DashedLine, color=YELLOW)
        vline11 = self.get_vertical_line_to_graph(3,func2,DashedLine, color=YELLOW)
        vlines = VGroup(vline1,vline2,vline3,vline4,vline5,vline6,vline7,vline8,vline9,vline10,vline11)

        hline1 = self.get_graph(lambda x: -3, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline2 = self.get_graph(lambda x: -2, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline3 = self.get_graph(lambda x: -1, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline4 = self.get_graph(lambda x: 0, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline5 = self.get_graph(lambda x: 1, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline6 = self.get_graph(lambda x: 2, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline7 = self.get_graph(lambda x: 3, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline8 = self.get_graph(lambda x: 4, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline9 = self.get_graph(lambda x: 5, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)
        hline10 = self.get_graph(lambda x: 6, x_min=-1.5, x_max=3.5, color=RED).set_opacity(0.5)

        hlines = VGroup(hline1,hline2,hline3,hline4,hline5,hline6,hline7,hline8,hline9,hline10)

        stack1 = Line(self.coords_to_point(-1,-4),
                      self.coords_to_point(-1,-7))
        stack2 = Line(self.coords_to_point(2-math.sqrt(8),-4),
                      self.coords_to_point(2-math.sqrt(8),-7))
        stack3 = Line(self.coords_to_point(2-math.sqrt(7),-4),
                      self.coords_to_point(2-math.sqrt(7),-7))
        stack4 = Line(self.coords_to_point(2-math.sqrt(6),-4),
                      self.coords_to_point(2-math.sqrt(6),-7))
        stack5 = Line(self.coords_to_point(2-math.sqrt(5),-4),
                      self.coords_to_point(2-math.sqrt(5),-7))
        stack6 = Line(self.coords_to_point(0,-4),
                      self.coords_to_point(0,-7))
        stack7 = Line(self.coords_to_point(2-math.sqrt(3),-4),
                      self.coords_to_point(2-math.sqrt(3),-7))
        stack8 = Line(self.coords_to_point(2-math.sqrt(2),-4),
                      self.coords_to_point(2-math.sqrt(2),-7))
        stack9 = Line(self.coords_to_point(1,-4),
                      self.coords_to_point(1,-7))
        stack10 = Line(self.coords_to_point(2,-4),
                      self.coords_to_point(2,-7)).set_color(color=YELLOW)
        stack11 = Line(self.coords_to_point(3,-4),
                      self.coords_to_point(3,-7))
        stacks = VGroup(stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9,stack10,stack11).set_opacity(0.5)

        arrow1 = Arrow(self.coords_to_point(-1,-5.6),self.coords_to_point(-1+0.1,-5.6),buff=0)
        arrow2 = Arrow(self.coords_to_point(2-math.sqrt(8),-5.6),self.coords_to_point(2-math.sqrt(8)+0.1,-5.6),buff=0)
        arrow3 = Arrow(self.coords_to_point(2-math.sqrt(7),-5.6),self.coords_to_point(2-math.sqrt(7)+0.1,-5.6),buff=0)
        arrow4 = Arrow(self.coords_to_point(2-math.sqrt(6),-5.6),self.coords_to_point(2-math.sqrt(6)+0.1,-5.6),buff=0)
        arrow5 = Arrow(self.coords_to_point(2-math.sqrt(5),-5.6),self.coords_to_point(2-math.sqrt(5)+0.1,-5.6),buff=0)
        arrow6 = Arrow(self.coords_to_point(2-math.sqrt(4),-5.6),self.coords_to_point(2-math.sqrt(4)+0.1,-5.6),buff=0)
        arrow7 = Arrow(self.coords_to_point(2-math.sqrt(3),-5.6),self.coords_to_point(2-math.sqrt(3)+0.1,-5.6),buff=0)
        arrow8 = Arrow(self.coords_to_point(2-math.sqrt(2),-5.6),self.coords_to_point(2-math.sqrt(2)+0.1,-5.6),buff=0)
        arrow9 = Arrow(self.coords_to_point(1,-5.6),self.coords_to_point(1+0.1,-5.6),buff=0)
        arrow10 = Arrow(self.coords_to_point(2,-5.6),self.coords_to_point(2+0.1,-5.6),buff=0).set_color(color=YELLOW)
        arrow11 = Arrow(self.coords_to_point(2,-5.6),self.coords_to_point(2-0.1,-5.6),buff=0).set_color(color=YELLOW)
        arrow12 = Arrow(self.coords_to_point(3,-5.6),self.coords_to_point(3-0.1,-5.6),buff=0)

        arrows = VGroup(arrow1,arrow2,arrow3,arrow4,arrow5,arrow6,arrow7,arrow8,arrow9,arrow10,arrow11,arrow12).set_opacity(0.5)

        func3 = func1.copy()

        self.play(ShowCreation(func1),Write(text18))
        self.wait(2)
        self.play(Transform(func1,func2),Transform(text18,text19))
        self.wait(2)
        self.play(ShowCreation(hlines))
        self.wait(3)
        self.play(ShowCreation(vlines))
        self.wait(3)
        self.play(ShowCreation(stacks),ShowCreation(arrows),FadeOut(hlines),Write(text20))
        self.wait(6)
        self.play(FadeOut(func1),FadeOut(text18),FadeOut(text20),FadeOut(vlines),FadeOut(stacks),FadeOut(self.axes),FadeOut(arrows))

        text21 = Text("If F(x) is the scalar potential for f(x)").move_to(UP*1.5)
        text22 = MathTex(r"\textrm{then} &\int_{a}^{b}f(x)dx \\ = &\int_{a}^{b}dF").scale(1.5).next_to(text21,DOWN)
        text23 = Text("The value of the integral is the number").move_to(UP)
        text24 = Text("of stacks of dF we cross on our path").next_to(text23,DOWN)
        self.play(Write(text21),Write(text22))
        self.wait(3)
        self.play(FadeOut(text21),FadeOut(text22))
        self.play(Write(text23),Write(text24))
        self.wait(3)
        self.play(FadeOut(text23),FadeOut(text24))

        area = self.get_riemann_rectangles(func3,-1,3,dx=0.005, input_sample_type='right', stroke_width=0, stroke_color='#000000', fill_opacity=0.5)
        lowerbound = self.get_vertical_line_to_graph(-1,func1,DashedLine,color=YELLOW)
        upperbound = self.get_vertical_line_to_graph(3,func1,DashedLine,color=YELLOW)
        path1 = Arrow(self.coords_to_point(-1,-5),self.coords_to_point(3,-5),color=BLUE,buff=0)
        path2 = Arrow(self.coords_to_point(3,-6.2),self.coords_to_point(-1,-6.2),color=RED,buff=0)

        text25 = MathTex(r"\int_{-1}^3 f(x)dx = 8").move_to(self.coords_to_point(4.5,6))
        text26 = MathTex("dF(",r"\vec p",")=9-1=8").move_to(self.coords_to_point(4.5,-5))
        text26[1].set_color(color=BLUE)
        text27 = MathTex("dF(",r"-\vec p",")=1-9=-8").move_to(self.coords_to_point(4.5,-6.2))
        text27[1].set_color(color=RED)
        text28 = MathTex(r"\int_3^{-1} f(x)dx = -8").move_to(self.coords_to_point(4.5,3))

        self.play(ShowCreation(self.axes),ShowCreation(func3),ShowCreation(stacks),ShowCreation(arrows),Write(text18),Write(text20))
        self.wait(3)
        self.play(ShowCreation(lowerbound),ShowCreation(upperbound),ShowCreation(area),ShowCreation(path1),Transform(text18,text25),Transform(text20,text26))
        self.wait(6)
        self.play(ShowCreation(path2),Write(text27),Write(text28))
        self.wait(6)

class Scene6 (ThreeDScene):
    def construct(self):

        text1 = Text("We can extend this to 3D!")
        text2 = MathTex(r"\textrm{Let }","f(x,y)",r"\textrm{ be a surface in space}").scale(2)

        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait(3)
        self.play(FadeOut(text2))

        axes = ThreeDAxes(z_min=-2,z_max=4,x_min=-7,x_max=7,y_min=-7,y_max=7)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def f(u,v):
            return np.array([u,v,0])
        plane = ParametricSurface(
            f,
            resolution=(22,22),
            v_min=-3,
            v_max=+3,
            u_min=-3,
            u_max=+3
        )
        plane2 =plane.copy().set_opacity(0)
        def g(u,v):
            return np.array([u,v,(0.5*u**2 + 0.5*v**2)-2])
        surface = ParametricSurface(
            g,
            resolution=(22,22),
            v_min=-3,
            v_max=+3,
            u_min=-3,
            u_max=+3
        )
        surface.set_style(fill_opacity=1)
        surface.set_style(stroke_color=PURPLE)
        surface.set_fill_by_checkerboard(PURPLE, BLUE, opacity=0.1)

        level1 = ParametricSurface(
            lambda x, y : np.array([x,y,-2]),
            resolution=(22,22),
            v_min=-1.5,
            v_max=+1.5,
            u_min=-1.5,
            u_max=+1.5,
            opacity=0.2
        )

        level2 = ParametricSurface(
            lambda x, y : np.array([x,y,-1]),
            resolution=(22,22),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
            opacity=0.2
        )

        level3 = ParametricSurface(
            lambda x, y : np.array([x,y,0]),
            resolution=(22,22),
            v_min=-2.5,
            v_max=+2.5,
            u_min=-2.5,
            u_max=+2.5,
            opacity=0.2
        )

        level4 = ParametricSurface(
            lambda x, y : np.array([x,y,1]),
            resolution=(22,22),
            v_min=-3,
            v_max=+3,
            u_min=-3,
            u_max=+3,
            opacity=0.2
        )

        level5 = ParametricSurface(
            lambda x, y : np.array([x,y,2]),
            resolution=(22,22),
            v_min=-3.5,
            v_max=+3.5,
            u_min=-3.5,
            u_max=+3.5,
            opacity=0.2
        )

        level6 = ParametricSurface(
            lambda x, y : np.array([x,y,3]),
            resolution=(22,22),
            v_min=-4,
            v_max=+4,
            u_min=-4,
            u_max=+4,
            opacity=0.2
        )

        circle1 = Dot([0,0,-2]).set_color(color=RED)

        circle2 = ParametricFunction(
            lambda u: np.array([math.sqrt(2)*np.cos(u),math.sqrt(2)*np.sin(u),-1]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle3 = ParametricFunction(
            lambda u: np.array([2*np.cos(u),2*np.sin(u),0]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle4 = ParametricFunction(
            lambda u: np.array([math.sqrt(6)*np.cos(u),math.sqrt(6)*np.sin(u),1]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle5 = ParametricFunction(
            lambda u: np.array([math.sqrt(8)*np.cos(u),math.sqrt(8)*np.sin(u),2]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle6 = ParametricFunction(
            lambda u: np.array([math.sqrt(10)*np.cos(u),math.sqrt(10)*np.sin(u),3]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle7 = ParametricFunction(
            lambda u: np.array([math.sqrt(12)*np.cos(u),math.sqrt(12)*np.sin(u),4]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle8 = ParametricFunction(
            lambda u: np.array([math.sqrt(14)*np.cos(u),math.sqrt(14)*np.sin(u),5]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle9 = ParametricFunction(
            lambda u: np.array([math.sqrt(16)*np.cos(u),math.sqrt(16)*np.sin(u),6]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle10 = ParametricFunction(
            lambda u: np.array([math.sqrt(18)*np.cos(u),math.sqrt(18)*np.sin(u),7]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle11 = ParametricFunction(
            lambda u: np.array([math.sqrt(20)*np.cos(u),math.sqrt(20)*np.sin(u),8]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle12 = ParametricFunction(
            lambda u: np.array([math.sqrt(22)*np.cos(u),math.sqrt(22)*np.sin(u),9]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle13 = ParametricFunction(
            lambda u: np.array([math.sqrt(24)*np.cos(u),math.sqrt(24)*np.sin(u),10]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle14 = ParametricFunction(
            lambda u: np.array([math.sqrt(26)*np.cos(u),math.sqrt(26)*np.sin(u),11]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle15 = ParametricFunction(
            lambda u: np.array([math.sqrt(28)*np.cos(u),math.sqrt(28)*np.sin(u),12]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle16 = ParametricFunction(
            lambda u: np.array([math.sqrt(30)*np.cos(u),math.sqrt(30)*np.sin(u),13]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle17 = ParametricFunction(
            lambda u: np.array([math.sqrt(32)*np.cos(u),math.sqrt(32)*np.sin(u),14]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle18 = ParametricFunction(
            lambda u: np.array([math.sqrt(34)*np.cos(u),math.sqrt(34)*np.sin(u),15]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        circle19 = ParametricFunction(
            lambda u: np.array([math.sqrt(36)*np.cos(u),math.sqrt(36)*np.sin(u),16]),
            t_min=0,
            t_max=2*3.15
        ).set_color(color=RED)

        text3 = MathTex(r"f(x,y)=\frac{1}{2}x^2+\frac{1}{2}y^2 -2")
        text3.to_corner(UL)

        self.add(axes)
        self.play(Write(plane))
        self.add_fixed_in_frame_mobjects(text3)
        self.play(Transform(plane,surface))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(text3),FadeOut(axes),FadeOut(plane))

        text4 = Text("You may have learned about").move_to(UP*1.5)
        text5 = Text("the gradient of a function.").next_to(text4,DOWN)
        text6 = MathTex(r"\nabla f = \frac {\partial f}{\partial x}\vec e_x + \frac {\partial f}{\partial y}\vec e_y").next_to(text5,DOWN*1.5).scale(1.5)
        self.add_fixed_in_frame_mobjects(text4,text5,text6)
        self.wait(6)
        self.play(FadeOut(text4),FadeOut(text5),FadeOut(text6))

        text7 = Text("Which gives us a vector field that").move_to(UP*1.5)
        text8 = Text("tells us the slope of the surface").next_to(text7,DOWN)
        text9 = Text("in the direction of steepest ascent.").next_to(text8,DOWN)
        text10 = MathTex(r"\nabla f = x \vec e_x + y \vec e_y").to_corner(UR)
        self.add_fixed_in_frame_mobjects(text7,text8,text9)
        self.wait(6)
        self.play(FadeOut(text7),FadeOut(text8),FadeOut(text9))

        vf = VectorField(
            lambda x : np.array([0.4*x[0],0.4*x[1]]),
            delta_x=0.5,
            delta_y=0.5,
            min_magnitude=0.8,
            max_magnitude=2,
            colors=[BLUE,GREEN,YELLOW,ORANGE,RED])
        self.play(ShowCreation(axes),ShowCreation(surface))
        self.wait()
        self.play(ShowCreation(vf))
        self.add_fixed_in_frame_mobjects(text10)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(text10),FadeOut(axes),FadeOut(surface),FadeOut(vf))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        text11 = Text("This is closely related to df").move_to(UP*2)
        text12 = MathTex(r"\nabla f = \frac {\partial f}{\partial x}\vec e_x + \frac {\partial f}{\partial y}\vec e_y").move_to(UP*0.5).scale(1.5)
        text13 = MathTex(r"df=\frac {\partial f}{\partial x} dx +\frac{\partial f}{\partial y} dy").move_to(DOWN*2).scale(1.5)
        text14 = MathTex(r"\nabla f = x \vec e_x + y \vec e_y").move_to(UP*0.5).scale(1.5)
        text15 = MathTex(r"df=xdx+ydy").move_to(DOWN*1.1).scale(1.5)
        text16 = MathTex(r"*\,f(x,y)=\frac{1}{2}x^2+\frac{1}{2}y^2 -2").move_to(DOWN*2.1)

        self.add_fixed_in_frame_mobjects(text11,text12,text13)
        self.wait(5)
        self.play(Transform(text12,text14),Transform(text13,text15))
        self.add_fixed_in_frame_mobjects(text16)
        self.wait(3)
        self.play(FadeOut(text11),FadeOut(text12),FadeOut(text13),FadeOut(text16))

        self.play(ShowCreation(axes),ShowCreation(surface))
        self.play(Write(level1),run_time=0.75)
        self.play(ShowCreation(circle1))
        self.play()
        self.play(Write(level2),FadeOut(level1),run_time=0.75)
        self.play(ShowCreation(circle2))
        self.play(Write(level3),FadeOut(level2),run_time=0.75)
        self.play(ShowCreation(circle3))
        self.play(Write(level4),FadeOut(level3),run_time=0.75)
        self.play(ShowCreation(circle4))
        self.play(Write(level5),FadeOut(level4),run_time=0.75)
        self.play(ShowCreation(circle5))
        self.play(Write(level6),FadeOut(level5),run_time=0.75)
        self.play(ShowCreation(circle6))
        self.play(FadeOut(level6),run_time=0.75)
        self.play(ShowCreation(circle7),ShowCreation(circle8),ShowCreation(circle9),ShowCreation(circle10),ShowCreation(circle11),ShowCreation(circle12),ShowCreation(circle13),ShowCreation(circle14),ShowCreation(circle15),ShowCreation(circle16),ShowCreation(circle17),ShowCreation(circle18),ShowCreation(circle19))

        path1 = ParametricFunction(
            lambda t : np.array([0,0,t]),
            t_min= -2,t_max=0
        ).set_opacity(0)

        path2 = ParametricFunction(
            lambda t : np.array([0,0,t]),
            t_min= -1,t_max=0
        ).set_opacity(0)

        path4 = ParametricFunction(
            lambda t : np.array([0,0,1-t]),
            t_min= 0,t_max=1
        ).set_opacity(0)

        path5 = ParametricFunction(
            lambda t : np.array([0,0,2-t]),
            t_min= 0,t_max=2
        ).set_opacity(0)

        path6 = ParametricFunction(
            lambda t : np.array([0,0,3-t]),
            t_min= 0,t_max=3
        ).set_opacity(0)

        path7 = ParametricFunction(
            lambda t : np.array([0,0,4-t]),
            t_min= 0,t_max=4
        ).set_opacity(0)

        path8 = ParametricFunction(
            lambda t : np.array([0,0,5-t]),
            t_min= 0,t_max=5
        ).set_opacity(0)

        path9 = ParametricFunction(
            lambda t : np.array([0,0,6-t]),
            t_min= 0,t_max=6
        ).set_opacity(0)

        path10 = ParametricFunction(
            lambda t : np.array([0,0,7-t]),
            t_min= 0,t_max=7
        ).set_opacity(0)

        path11 = ParametricFunction(
            lambda t : np.array([0,0,8-t]),
            t_min= 0,t_max=8
        ).set_opacity(0)

        path12 = ParametricFunction(
            lambda t : np.array([0,0,9-t]),
            t_min= 0,t_max=9
        ).set_opacity(0)

        path13 = ParametricFunction(
            lambda t : np.array([0,0,10-t]),
            t_min= 0,t_max=10
        ).set_opacity(0)

        path14 = ParametricFunction(
            lambda t : np.array([0,0,11-t]),
            t_min= 0,t_max=11
        ).set_opacity(0)

        path15 = ParametricFunction(
            lambda t : np.array([0,0,12-t]),
            t_min= 0,t_max=12
        ).set_opacity(0)

        path16 = ParametricFunction(
            lambda t : np.array([0,0,13-t]),
            t_min= 0,t_max=13
        ).set_opacity(0)

        path17 = ParametricFunction(
            lambda t : np.array([0,0,14-t]),
            t_min= 0,t_max=14
        ).set_opacity(0)

        path18 = ParametricFunction(
            lambda t : np.array([0,0,15-t]),
            t_min= 0,t_max=15
        ).set_opacity(0)

        path19 = ParametricFunction(
            lambda t : np.array([0,0,16-t]),
            t_min= 0,t_max=16
        ).set_opacity(0)

        self.add(path1,path2,path4,path5,path6,path7,path8,path9,path10,path11,path12,path13,path14,path15,path16,path17,path18,path19)

        self.play(
            MoveAlongPath(circle1,path1),
            MoveAlongPath(circle2,path2),
            MoveAlongPath(circle4,path4),
            MoveAlongPath(circle5,path5),
            MoveAlongPath(circle6,path6),
            MoveAlongPath(circle7,path7),
            MoveAlongPath(circle8,path8),
            MoveAlongPath(circle9,path9),
            MoveAlongPath(circle10,path10),
            MoveAlongPath(circle11,path11),
            MoveAlongPath(circle12,path12),
            MoveAlongPath(circle13,path13),
            MoveAlongPath(circle14,path14),
            MoveAlongPath(circle15,path15),
            MoveAlongPath(circle15,path16),
            MoveAlongPath(circle15,path17),
            MoveAlongPath(circle15,path18),
            MoveAlongPath(circle15,path19),
            Transform(surface,plane2)
        )
        self.move_camera(phi= 0*DEGREES, theta=-90*DEGREES)
        text17 = MathTex(r"df\,\,\,").scale(2).to_corner(UR)
        text17[0].set_color(RED)
        self.play(Write(text17))
        self.wait(3)
        text18 = MathTex(r"\nabla f").scale(2).to_corner(UR).set_color(BLUE)
        self.wait(3)
        self.play(
            FadeOut(circle1),
            FadeOut(circle2),
            FadeOut(circle3),
            FadeOut(circle4),
            FadeOut(circle5),
            FadeOut(circle6),
            FadeOut(circle7),
            FadeOut(circle8),
            FadeOut(circle9),
            FadeOut(circle10),
            FadeOut(circle11),
            FadeOut(circle12),
            FadeOut(circle13),
            FadeOut(circle14),
            FadeOut(circle15),
            FadeOut(circle16),
            FadeOut(circle17),
            FadeOut(circle18),
            FadeOut(circle19),
            GrowFromCenter(vf),
            Transform(text17,text18)
        )
        self.wait(3)

class Scene7 (ThreeDScene):
    def construct(self):
        text00 = Text("We can reinterpret the directional").move_to(UP*1.5)
        text01 = Text("derivative in terms of differential").next_to(text00,DOWN)
        text02 = Text("forms as well").next_to(text01,DOWN)

        self.play(Write(text00),Write(text01),Write(text02))
        self.wait(3)
        self.play(FadeOut(text00),FadeOut(text01),FadeOut(text02))

        text1 = Text("Traditionally we compute the").move_to(UP*2.5)
        text2 = Text("directional derivative of a function").next_to(text1,DOWN)
        text3 = Text("using the gradient at a point and").next_to(text2,DOWN)
        text4 = Text("taking the dot product with a vector.").next_to(text3,DOWN)
        text5 = MathTex(r"\nabla_{\vec v}f = \nabla f(x,y) \cdot \vec v").move_to(DOWN*1.5).scale(2)

        self.play(Write(text1),Write(text2),Write(text3),Write(text4),Write(text5))
        self.wait(7)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text5))

        text6 = Text("We can think of this as taking a plane").move_to(UP*2.5)
        text7 = Text("spanned by the z axis and our vector").next_to(text6,DOWN)
        text8 = Text("and slicing through the surface to get").next_to(text7,DOWN)
        text9 = Text("a curve of intersection and then taking").next_to(text8,DOWN)
        text10= Text("the derivative at that point.").next_to(text9,DOWN)

        self.play(Write(text6),Write(text7),Write(text8),Write(text9),Write(text10))
        self.wait(7)
        self.play(FadeOut(text6),FadeOut(text7),FadeOut(text8),FadeOut(text9),FadeOut(text10))

        axes = ThreeDAxes(z_min=-1,z_max=+6,x_min=-7,x_max=+7,y_min=-7,y_max=+7)
        surface = ParametricSurface(
            lambda u,v : np.array([u,v,u*0.5 +0.25*(v**2)]),
            resolution=(22,22),
            v_min=-6,v_max=+6,u_min=-6,u_max=+6
        )

        surface.set_style(fill_opacity=1)
        surface.set_style(stroke_color=PURPLE)
        surface.set_fill_by_checkerboard(PURPLE, BLUE, opacity=0.15)

        vf = VectorField(
            lambda x : np.array([0.5,0.5*x[1]]),
            delta_x=0.5,
            delta_y=0.5,
            min_magnitude=0.8,
            max_magnitude=2,
            colors=[BLUE,GREEN,YELLOW,ORANGE,RED])

        text7 = MathTex(r"f(x,y)=\frac{1}{2} x +\frac{1}{4}y^2").to_corner(UR)
        text8 = MathTex(r"\nabla f(x,y)=\frac{1}{2}\hat{i}+ \frac{1}{2}y\hat{j} +1").to_corner(DR)

        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.move_camera(frame_center=[0,0,1])
        self.play(Write(axes))
        self.play(Write(surface))
        self.add_fixed_in_frame_mobjects(text7)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
        self.play(ShowCreation(vf))
        self.add_fixed_in_frame_mobjects(text8)
        self.wait(5.5)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(vf))

        text9 = MathTex(r"f(4,2)=3").set_color(YELLOW).to_corner(UR)
        text10 = MathTex(r"\nabla f(4,2)=\frac{1}{2}\hat{i}+ 1\hat{j}").to_corner(DR).set_color(GREEN)
        direction1 = Arrow([4,2,0],[4.5,3,0],buff=0,color=GREEN)
        direction2 = Arrow([4,2,0],[4+2/math.sqrt(5),2+1/math.sqrt(5),0],buff=0,color=BLUE)
        vline = Line([4,2,0],[4,2,3],color=YELLOW)
        hline1 = Line([4,0,0],[4,2,0],color=WHITE)
        hline2 = Line([0,2,0],[4,2,0],color=WHITE)
        dot1 = Dot([4,2,0],color=WHITE)
        dot2 = Dot([4,2,3],color=YELLOW)

        self.play(ShowCreation(hline1),ShowCreation(hline2),ShowCreation(dot1))
        self.play(ShowCreation(vline),ShowCreation(dot2),Transform(text7,text9))
        self.wait()
        self.play(ShowCreation(direction1),Transform(text8,text10))
        self.wait()


        intersect1 = ParametricSurface(
            lambda u,v :
                np.array([
                    4+2*u,
                    2+u,
                    v
                ]),
            u_min=-6.5,u_max=2,v_min=-1,v_max=6
        )
        intersect1.set_style(fill_opacity=1)
        intersect1.set_style(stroke_color=BLUE)
        intersect1.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.7)

        intersect2 = ParametricFunction(
            lambda u :
                np.array([
                    4+2*u,
                    2+u,
                    0.25*u**2 +2*u +3
                ]),
            t_min=-6.5,t_max=2,color=RED
        )
        tangent1=ParametricFunction(
            lambda u :
                np.array([
                    4+2*u/math.sqrt(5),
                    2+u/math.sqrt(5),
                    3+2/math.sqrt(5)*u
                ]),
            t_min=-2,t_max=2,color=BLUE
        )

        vtext = MathTex(r"\vec v = \frac{2}{\sqrt{5}}\hat{i}+\frac{1}{\sqrt{5}}\hat{j}").to_corner(DL).set_color(BLUE)
        self.wait(2)
        self.play(ShowCreation(direction2))
        self.add_fixed_in_frame_mobjects(vtext)
        self.wait(2)
        self.play(Write(intersect1))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
        self.play(Write(intersect2))
        self.wait(1.5)
        self.play(Write(tangent1))
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(intersect1))
        self.wait(2)
        self.play(FadeOut(text7),FadeOut(text8),FadeOut(vtext),FadeOut(direction1),FadeOut(direction2))
        self.wait(2)
        self.play(Uncreate(hline1),Uncreate(hline2),Uncreate(vline),Uncreate(dot1),Uncreate(dot2),Uncreate(tangent1),Uncreate(intersect2))
        self.wait()

        text11 = Text("We can also interpret the directional").move_to(UP)
        text12 = Text("derivative in terms of differential forms.").next_to(text11,DOWN)
        rectangle = Rectangle(width=16,height=2,color=BLACK,fill_opacity=1).move_to([0,0.5,0])
        self.add(rectangle,text11,text12)

        self.add_fixed_in_frame_mobjects(rectangle,text11,text12)
        self.wait(2)
        self.play(FadeOut(text11),FadeOut(text12),FadeOut(rectangle))

        slice1 = ParametricSurface(
            lambda u,v : np.array([u,v,-5]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        slice2 = ParametricSurface(
            lambda u,v : np.array([u,v,-3]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        slice3 = ParametricSurface(
            lambda u,v : np.array([u,v,-2]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        slice4 = ParametricSurface(
            lambda u,v : np.array([u,v,-1]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        slice5 = ParametricSurface(
            lambda u,v : np.array([u,v,0]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        slice6 = ParametricSurface(
            lambda u,v : np.array([u,v,1]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        slice7 = ParametricSurface(
            lambda u,v : np.array([u,v,2]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        slice8 = ParametricSurface(
            lambda u,v : np.array([u,v,3]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )
        slice9 = ParametricSurface(
            lambda u,v : np.array([u,v,4]),
            u_min=-15,u_max=15,v_min=-15,v_max=15,color=BLUE,resolution=(15,15)
        )

        levelsets = VGroup(
            ParametricFunction(
                lambda u: np.array([-0.5*u**2-6,u,-3]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2-4,u,-2]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2-2,u,-1]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2,u,0]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+2,u,1]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+4,u,2]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+6,u,3]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+8,u,4]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+10,u,5]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+12,u,6]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+14,u,7]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+16,u,8]),
                t_min=-5,t_max=5,color=RED
            )
        )
        paths = VGroup(
            ParametricFunction(
                lambda u: np.array([
                    levelsets[0].get_center()[0],
                    levelsets[0].get_center()[1],
                    levelsets[0].get_center()[2]-levelsets[0].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[1].get_center()[0],
                    levelsets[1].get_center()[1],
                    levelsets[1].get_center()[2]-levelsets[1].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[2].get_center()[0],
                    levelsets[2].get_center()[1],
                    levelsets[2].get_center()[2]-levelsets[2].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[3].get_center()[0],
                    levelsets[3].get_center()[1],
                    levelsets[3].get_center()[2]-levelsets[3].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[4].get_center()[0],
                    levelsets[4].get_center()[1],
                    levelsets[4].get_center()[2]-levelsets[4].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[5].get_center()[0],
                    levelsets[5].get_center()[1],
                    levelsets[5].get_center()[2]-levelsets[5].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[6].get_center()[0],
                    levelsets[6].get_center()[1],
                    levelsets[6].get_center()[2]-levelsets[6].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[7].get_center()[0],
                    levelsets[7].get_center()[1],
                    levelsets[7].get_center()[2]-levelsets[7].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[8].get_center()[0],
                    levelsets[8].get_center()[1],
                    levelsets[8].get_center()[2]-levelsets[8].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[9].get_center()[0],
                    levelsets[9].get_center()[1],
                    levelsets[9].get_center()[2]-levelsets[9].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[10].get_center()[0],
                    levelsets[10].get_center()[1],
                    levelsets[10].get_center()[2]-levelsets[10].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            ),

            ParametricFunction(
                lambda u: np.array([
                    levelsets[11].get_center()[0],
                    levelsets[11].get_center()[1],
                    levelsets[11].get_center()[2]-levelsets[11].get_center()[2]*u
                    ]),
                t_min=0,t_max=1
            )
        ).set_opacity(0)
        self.add(paths)
        self.play(Write(slice1))
        self.play(Write(levelsets[0]))
        self.play(FadeOut(slice1))
        self.play(Write(slice2))
        self.play(Write(levelsets[1]))
        self.play(FadeOut(slice2))
        self.play(Write(slice3))
        self.play(Write(levelsets[2]))
        self.play(FadeOut(slice3))
        self.play(Write(slice4))
        self.play(Write(levelsets[3]))
        self.play(FadeOut(slice4))
        self.play(Write(slice5))
        self.play(Write(levelsets[4]))
        self.play(FadeOut(slice5))
        self.play(Write(slice6))
        self.play(Write(levelsets[5]))
        self.play(FadeOut(slice6))
        self.play(Write(slice7))
        self.play(Write(levelsets[6]))
        self.play(FadeOut(slice7))
        self.play(Write(slice8))
        self.play(Write(levelsets[7]))
        self.play(FadeOut(slice8))
        self.play(Write(slice9))
        self.play(Write(levelsets[8]))
        self.play(FadeOut(slice9))
        self.play(Write(levelsets[9]),Write(levelsets[10]),Write(levelsets[11]))
        self.wait()

        self.play(
            MoveAlongPath(levelsets[0],paths[0]),
            MoveAlongPath(levelsets[1],paths[1]),
            MoveAlongPath(levelsets[2],paths[2]),
            MoveAlongPath(levelsets[3],paths[3]),
            MoveAlongPath(levelsets[4],paths[4]),
            MoveAlongPath(levelsets[5],paths[5]),
            MoveAlongPath(levelsets[6],paths[6]),
            MoveAlongPath(levelsets[7],paths[7]),
            MoveAlongPath(levelsets[8],paths[8]),
            MoveAlongPath(levelsets[9],paths[9]),
            MoveAlongPath(levelsets[10],paths[10]),
            MoveAlongPath(levelsets[11],paths[11]),
            FadeOut(surface)
            )



        self.move_camera(phi= 0*DEGREES, theta=-90*DEGREES)
        self.play(FadeOut(axes))

class Scene8(MovingCameraScene):
    def construct(self):
        levelsets = VGroup(
            ParametricFunction(
                lambda u: np.array([-0.5*u**2-6,u,-3]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2-4,u,-2]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2-2,u,-1]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2,u,0]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+2,u,1]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+4,u,2]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+6,u,3]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+8,u,4]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+10,u,5]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+12,u,5]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+14,u,5]),
                t_min=-5,t_max=5,color=RED
            ),

            ParametricFunction(
                lambda u: np.array([-0.5*u**2+16,u,5]),
                t_min=-5,t_max=5,color=RED
            )
        )
        arrows = VGroup(
            Arrow([-6,0,0],[-5.5,0,0],buff=0,color=RED),
            Arrow([-4,0,0],[-3.5,0,0],buff=0,color=RED),
            Arrow([-2,0,0],[-1.5,0,0],buff=0,color=RED),
            Arrow([0,0,0],[0.5,0,0],buff=0,color=RED),
            Arrow([2,0,0],[2.5,0,0],buff=0,color=RED),
            Arrow([4,0,0],[4.5,0,0],buff=0,color=RED),
            Arrow([6,0,0],[6.5,0,0],buff=0,color=RED),
            Arrow([8,0,0],[8.5,0,0],buff=0,color=RED),
            Arrow([8,0,0],[10.5,0,0],buff=0,color=RED)
            )

        alpha1 = VGroup(
            ParametricFunction(
                lambda u : np.array([u+4+(-0.8),-0.5*u+2+(-1.6),0]),
                t_min=-1.3,t_max=1.3
            ),
            ParametricFunction(
                lambda u : np.array([u+4+(-0.4),-0.5*u+2+(-0.8),0]),
                t_min=-1.3,t_max=1.3
            ),
            ParametricFunction(
                lambda u : np.array([u+4,-0.5*u+2,0]),
                t_min=-1.3,t_max=1.3
            ),
            ParametricFunction(
                lambda u : np.array([u+4+(0.4),-0.5*u+2+(0.8),0]),
                t_min=-1.3,t_max=1.3
            ),
            ParametricFunction(
                lambda u : np.array([u+4+(0.8),-0.5*u+2+(1.6),0]),
                t_min=-1.3,t_max=1.3
            )
        ).set_opacity(1)
        alpha1[2].set_opacity(1)
        alpha2 = VGroup(
            Arrow([4+(-0.8),2+(-1.6),0],[4+(-0.8)+0.2,2+(-1.6)+0.4,0],buff=0),
            Arrow([4+(-0.4),2+(-0.8),0],[4+(-0.4)+0.2,2+(-0.8)+0.4,0],buff=0),
            Arrow([4,2,0],[4+0.2,2+0.4,0],buff=0),
            Arrow([4+(0.4),2+(0.8),0],[4+(0.4)+0.2,2+(0.8)+0.4,0],buff=0),
            Arrow([4+(0.8),2+(1.6),0],[4+(0.8)+0.2,2+(1.6)+0.4,0],buff=0)
        ).set_opacity(1)
        alpha2[2].set_opacity(1)

        dot = Dot([4,2,0])
        direction1 = Arrow([4,2,0],[4.5,3,0],buff=0,color=GREEN)
        direction2 = Arrow([4,2,0],[4+2/math.sqrt(5),2+1/math.sqrt(5),0],buff=0,color=BLUE)

        axes = NumberPlane()

        text1 = MathTex("df").set_color(RED).move_to([-0.5,0,0]).scale(1.2)
        text2 = MathTex(r"df",r"_{(4,2)}").move_to([6.3,1,0])
        text2[0].scale(1.2)
        text2[1].scale(0.8)
        text3 = MathTex(r"df",r"_p",r"(",r"\vec v",r")",r"=\frac{2}{\sqrt 5}").move_to([0,2,0])
        text3[0].set_color(RED).scale(1.2)
        text3[1].scale(0.9)
        text3[3].set_color(BLUE)

        rectangle = Rectangle(color=BLACK,fill_color=BLACK,fill_opacity=1,height=1.5,width=4).move_to(text3)

        self.add(levelsets)
        self.play(Write(arrows))
        self.wait(2)
        self.play(Write(text1))
        self.wait(2)
        self.play(self.camera.frame.animate.move_to([3,2,0]).scale(0.7))
        self.play(ShowCreation(dot),ShowCreation(alpha1),ShowCreation(alpha2),Write(text2))
        self.wait(3)
        self.play(ShowCreation(direction1))
        self.wait(2)
        self.play(Transform(direction1,direction2),Write(rectangle),Write(text3))
        self.wait(3)
