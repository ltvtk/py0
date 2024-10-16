import re
from antlr4 import *
from py0.generated.Py0Lexer import Py0Lexer
from py0.generated.Py0Parser import Py0Parser
from py0.generated.Py0Listener import Py0Listener

class Py0ToPythonTranspiler(Py0Listener):
    def __init__(self, input_stream):
        self.output = []
        self.indent = 0
        self.input_stream = input_stream
        self.current_line = -1

    def get_indent(self):
        return '    ' * self.indent

    def enterFunctionDecl(self, ctx: Py0Parser.FunctionDeclContext):
        func_header = self.get_expr_text(ctx)
        self.output.append(f"{self.get_indent()}def {func_header}:\n")
        self.indent += 1

    def exitFunctionDecl(self, ctx: Py0Parser.FunctionDeclContext):
        self.indent -= 1

    def enterForStatement(self, ctx: Py0Parser.ForStatementContext):
        expr = self.get_expr_text(ctx)
        self.output.append(f"{self.get_indent()}for {expr}:\n")
        self.indent += 1

    def exitForStatement(self, ctx: Py0Parser.ForStatementContext):
        self.indent -= 1

    def enterWhileStatement(self, ctx: Py0Parser.WhileStatementContext):
        expr = self.get_expr_text(ctx)
        self.output.append(f"{self.get_indent()}while {expr}:\n")
        self.indent += 1

    def exitWhileStatement(self, ctx: Py0Parser.WhileStatementContext):
        self.indent -= 1

    def enterRepeatStatement(self, ctx: Py0Parser.RepeatStatementContext):
        expr = self.get_expr_text(ctx)
        self.output.append(f"{self.get_indent()}for _ in range({expr}):\n")
        self.indent += 1

    def exitRepeatStatement(self, ctx: Py0Parser.RepeatStatementContext):
        self.indent -= 1

    def enterIfStatement(self, ctx: Py0Parser.IfStatementContext):
        expr = self.get_expr_text(ctx)
        self.output.append(f"{self.get_indent()}if {expr}:\n")
        self.indent += 1

    def exitIfStatement(self, ctx: Py0Parser.IfStatementContext):
        self.indent -= 1

    def enterElseIfStatement(self, ctx: Py0Parser.ElseIfStatementContext):
        expr = self.get_expr_text(ctx)
        self.indent -= 1
        self.output.append(f"{self.get_indent()}elif {expr}:\n")
        self.indent += 1

    def enterElseStatement(self, ctx: Py0Parser.ElseStatementContext):
        self.indent -= 1
        self.output.append(f"{self.get_indent()}else:\n")
        self.indent += 1

    def enterSimpleStatement(self, ctx: Py0Parser.SimpleStatementContext):
        start_index = ctx.start.start
        stop_index = ctx.stop.stop
        stmt = self.input_stream.getText(start_index, stop_index).strip()
        line_number = ctx.start.line
        if line_number != self.current_line:
            stmt = self.convert_arrow_function(stmt)
            self.output.append(f"{self.get_indent()}{stmt}\n")
            self.current_line = line_number

    def convert_arrow_function(self, stmt):
        # Patterns for different types of arrow functions
        pattern1 = r'^(\w+)\s*=\s*\(\s*(.*?)\s*\)\s*=>\s*(.*)$'
        pattern2 = r'^(\w+)\s*=\s*(\w+)\s*=>\s*(.*)$'
        pattern3 = r'^(\w+)\s*=\s*\(\s*\)\s*=>\s*(.*)$'
        pattern4 = r'(\w+\()?\(\((\w+)\)\s*=>\s*(.*?)\)\((.+?)\)\)?'

        if '=>' in stmt:
            # Check for immediately invoked arrow function
            match = re.search(pattern4, stmt)
            if match:
                outer_func = match.group(1) or ''
                param = match.group(2)
                body = match.group(3)
                arg = match.group(4)
                closing_paren = ')' if outer_func else ''
                return f"{outer_func}(lambda {param}: {body})({arg}){closing_paren}"
            
            # Check for other arrow function declaration cases
            match = re.match(pattern1, stmt)
            if match:
                var_name = match.group(1)
                params = match.group(2)
                body = match.group(3)
                return f"{var_name} = lambda {params}: {body}"
            match = re.match(pattern2, stmt)
            if match:
                var_name = match.group(1)
                param = match.group(2)
                body = match.group(3)
                return f"{var_name} = lambda {param}: {body}"
            match = re.match(pattern3, stmt)
            if match:
                var_name = match.group(1)
                body = match.group(2)
                return f"{var_name} = lambda: {body}"
        return stmt

    def get_expr_text(self, ctx):
        start_index = ctx.expr().start.start
        stop_index = ctx.expr().stop.stop
        return self.input_stream.getText(start_index, stop_index).strip()

    def getOutput(self):
        return ''.join(self.output)

def transpile_file(input_file, output_file):
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = Py0Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Py0Parser(stream)
    tree = parser.program()

    transpiler = Py0ToPythonTranspiler(input_stream)
    walker = ParseTreeWalker()
    walker.walk(transpiler, tree)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transpiler.getOutput())

if __name__ == "__main__":
    transpile_file("input.py0", "output.py")