from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 E aí, fã da FURIA! Eu sou o *FURIA Bot*, seu parceiro nos jogos de CS:GO.\n\nDigite /menu para ver tudo que posso fazer!",
        parse_mode="Markdown"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 *Menu FURIA Fans* 🔥\n"
        "/proximojogo - Quando e contra quem jogamos\n"
        "/ultimojogo - Resultado do último confronto\n"
        "/elenco - Quem está jogando na FURIA\n"
        "/curiosidades - Fatos legais sobre a FURIA\n"
        "/quiz - Teste seu conhecimento sobre o time\n"
        "/redessociais - Links oficiais\n"
        "/apoie - Demonstre seu apoio! 🖤",
        parse_mode="Markdown"
    )

async def proximojogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 O próximo jogo da FURIA é contra a NAVI, dia 26/04 às 18h!")

async def ultimojogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 Última partida: FURIA 2 x 1 MIBR — GG demais!")

async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://files.fm/u/cn9rwp9w4u",
        caption=(
            "🎮 *Elenco atual da FURIA:*\n"
            "- arT (IGL)\n"
            "- yuurih (Rifler)\n"
            "- KSCERATO (Rifler)\n"
            "- chelo (Entry)\n"
            "- FalleN (AWPer)\n"
        ),
        parse_mode="Markdown"
    )


async def curiosidades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🐾 Sabia que a FURIA foi fundada em 2017 e já venceu mais de 20 títulos nacionais e internacionais?")

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ 2015", callback_data="resposta_errada")],
        [InlineKeyboardButton("2️⃣ 2017", callback_data="resposta_certa")],
        [InlineKeyboardButton("3️⃣ 2019", callback_data="resposta_errada")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

from telegram.ext import CallbackQueryHandler

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "resposta_certa":
        await query.edit_message_caption(
            caption="✅ *Acertou!*\nA FURIA foi fundada em 2017. GG! 🎉",
            parse_mode="Markdown"
        )
    else:
        await query.edit_message_caption(
            caption="❌ *Errou!*\nA resposta certa é 2017. Bora aprender mais sobre o time! 💪",
            parse_mode="Markdown"
        )

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("1️⃣ 2015", callback_data="resposta_errada")],
        [InlineKeyboardButton("2️⃣ 2017", callback_data="resposta_certa")],
        [InlineKeyboardButton("3️⃣ 2019", callback_data="resposta_errada")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_photo(
        photo="https://files.fm/u/2afvuvddhj",
        caption="❓ *Quiz FURIA:*\n\nEm que ano a FURIA foi fundada?",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )
    app.add_handler(CallbackQueryHandler(button_handler, pattern="resposta_certa|resposta_errada"))
    
async def resposta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Acertou! A FURIA foi fundada em 2017. GG!")

async def redessociais(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Siga a FURIA nas redes sociais:\n"
        "Instagram: https://instagram.com/furiagg\n"
        "Twitter: https://twitter.com/furiagg\n"
        "YouTube: https://youtube.com/FURIAgg"
    )

async def apoie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🖤 Mostre seu apoio! Poste #GoFURIA nas redes e marque @furiagg!\n\n🔥 A luta é nossa!")

from telegram.ext import MessageHandler, filters

# Handler para mensagens de texto comuns
async def responder_texto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.lower()

    if texto == "start":
        await start(update, context)
    elif texto == "menu":
        await menu(update, context)
    elif texto == "elenco":
        await elenco(update, context)
    elif texto == "próximo jogo" or texto == "proximo jogo":
        await proximojogo(update, context)
    elif texto == "último jogo" or texto == "ultimo jogo":
        await ultimojogo(update, context)
    elif texto == "curiosidades":
        await curiosidades(update, context)
    elif texto == "quiz":
        await quiz(update, context)
    elif texto.startswith("resposta"):
        await resposta(update, context)
    elif texto == "redes sociais":
        await redessociais(update, context)
    elif texto == "apoie":
        await apoie(update, context)

app = ApplicationBuilder().token("7986450035:AAHozXgJzSnYC7WA9EL2r7EMQ2V6yCX4qHQ").build()
# Adicione isso no final, junto com os outros handlers:
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder_texto))

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("proximojogo", proximojogo))
app.add_handler(CommandHandler("ultimojogo", ultimojogo))
app.add_handler(CommandHandler("elenco", elenco))
app.add_handler(CommandHandler("curiosidades", curiosidades))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(CommandHandler("resposta", resposta))
app.add_handler(CommandHandler("redessociais", redessociais))
app.add_handler(CommandHandler("apoie", apoie))

print("🤖 Bot está rodando... (Ctrl+C para parar)")
app.run_polling()
