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

        alpha5 = MathTex(r"\alpha","(",r"\vec v",")=","v^x",r"\alpha","(",r"\vec e_y",")+","v^y",r"\alpha","(",r"\vec e_y",")").next_to(text26,DOWN*2).scale(2)
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

class Scene5(Scene):
    def construct(self):
        self.wait()
