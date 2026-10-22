import streamlit as st


def brl(v: float) -> str:
    s = f"{v:,.2f}"
    return "R$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")


st.set_page_config(page_title="Calculadora de Taxas de Maquininha",
                   page_icon="💳", layout="centered")

st.title("Calculadora de Taxas de Maquininha")
st.caption("Quanto sobra de verdade em cada venda no cartão. Ferramenta educativa "
           "do Guia Maquininha — as taxas variam por adquirente, bandeira e negociação.")

esq, dir_ = st.columns(2)
with esq:
    valor = st.number_input("Valor da venda (R$)", min_value=0.0, value=100.0,
                            step=10.0, format="%.2f")
    taxa = st.number_input("Taxa da maquininha (%)", min_value=0.0, max_value=30.0,
                           value=3.49, step=0.01, format="%.2f")
with dir_:
    parcelas = st.number_input("Parcelas", min_value=1, max_value=12, value=1, step=1)

custo = valor * taxa / 100.0
liquido = valor - custo
parcela_liquida = liquido / parcelas
cobrar = valor / (1.0 - taxa / 100.0) if taxa < 100 else float("inf")
diferenca = cobrar - valor

st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Custo da taxa", brl(custo))
c2.metric("Líquido a receber", brl(liquido))
c3.metric("Cada parcela (líquida)", brl(parcela_liquida))

with st.expander("Quanto cobrar no cartão para não perder dinheiro?"):
    st.write(f"Para o valor líquido sair **igual ao preço de vista de {brl(valor)}**, "
             f"a venda no cartão precisa ser de **{brl(cobrar)}** "
             f"(diferença de {brl(diferenca)} = a taxa embutida).")
    st.caption("Fórmula: valor ÷ (1 − taxa). Em vendas parceladas, some também o custo "
               "do prazo de recebimento (dinheiro hoje vale mais que dinheiro em 30 dias).")

st.divider()
st.markdown("📈 [**Índice de Taxas de Maquininhas — histórico mensal por adquirente**]"
            "(https://guiamaquininha.com.br/indice-de-taxas/)")
st.caption("Guia Maquininha — comparador independente de maquininhas de cartão. "
           "Conteúdo educativo; confira sempre o contrato da sua adquirente.")
