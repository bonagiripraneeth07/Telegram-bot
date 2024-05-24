


import logging
from telegram import Update, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = "#API key goes here "
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
                                ~ Welcome to DevNavigator! 🤖
Hi there! I'm DevNavigator, your personal guide to the world of coding. Whether you're looking for top-notch YouTube tutorials, comprehensive roadmaps, or detailed notes, I've got you covered.

Got a question about programming languages, frameworks, or anything else related to coding? Just ask, and I'll do my best to help you out.

Let's embark on this coding journey together! 🚀



~ /getstarted  to get start 
    """)
async def getstarted(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="""
 ~ /roadmaps  - Roadmaps of popular languages   
 ~ /Youtube  - Popular Youtube channels on programming 
 ~ /Notes    - Notes on most demanding languages  
 ~ /Practice - practice on popular websites and get Certified 
 ~ /contact  - for Feedback  and more details... 
 ~/help      - Help   
    """)

    #start of  roadmaps
async def roadmaps(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    Here are the few popular language and  Role based Roadmaps:
    
    -ROLE BASED-
 ~/Frontend - Frontend developer
 ~/Backend  - Backend developer 
 ~/DevOps   -DevOps
 ~/FullStack - Full Stack developer
 ~/AIandDataScientist  - AI and Data Scientist developer 
 ~/DataAnalyst   -Data Analyst   
 ~/More  
    ~SKILL BASED ~
 ~/React_Roadmap - Reactjs
 ~/Angular_Roadmap - Angular
 ~/Nodejs_Roadmap  - Node.js
 ~/Python_Roadmap   -Python
 ~/Java_Roadmap   -Java
 ~/DSA_Roadmap   -DataStructures&Algorithms 
 ~/More
 
    
    """)



async def Fronted(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/frontend")
async def Backend(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/backend")
async def DevOps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/devops")
async def FullStack(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/full-stack")
async def AIandDataScientist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/ai-data-scientist")
async def DataAnalyst(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/data-analyst")
async  def More(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/roadmaps ")


async def React_Roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/react")
async def Angular_Road_map(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/angular")
async def Python_Roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/python ")


async def Nodejs_Roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/nodejs ")

async def Java_Roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/java ")


async def DSA_Roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/datastructures-and-algorithms ")
async def More(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://roadmap.sh/roadmaps ")




    #end of roadmaps

    #start of youtube

async def Youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
        Here are few popular Youtube channels for programming :
        
~/Python        - Python 
~/Java          - Java 
~/HTML_CSS      - HTML and CSS
~/Javascript    -Javascript
~/Androidstudio - Python 
~/C             - Python     
 ~/PostgreSQL   - Python    
    """)
async def Python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://www.youtube.com/playlist?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3")
async def Java (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://www.youtube.com/playlist?list=PLsyeobzWxl7pe_IiTfNyr55kwJPWbgxB5")
async def HTML_CSS(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=" https://youtu.be/G3e-cpL7ofc?si=7IEUiAbbR7uJEcR_")
async  def Javascript(update: Update, context: ContextTypes.DEFAULT_TYPE):
     await context.bot.send_message(chat_id=update.effective_chat.id,text="https://youtu.be/EerdGm-ehJQ?si=w8Rp35EO3MqIiXBX")
async def Androidstudio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://youtu.be/u64gyCdqawU?si=08E38ZSwiqSJvNYE")
async def C(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="https://youtube.com/playlist?list=PL6gx4Cwl9DGAKIXv8Yr6nhGJ9Vlcjyymq&si=RsfoNdOL6QCEljcr")
async def PostgreSQL(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="https://youtu.be/qw--VYLpxG4?si=80FnnUIJn4G_nKls")

    #end of youtube

    #start of notes
async def Notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=""" 
    Here are few websites from were you can get a Detailed Notes on different programming languages and Courses 
    
    ~ https://www.geeksforgeeks.org/ - Geeks for geeks
    ~ https://www.javatpoint.com/    - JavaTpoint
    ~https://www.w3schools.com/js/   -W3schools
    ~https://www.javascripttutorial.net/ -Javascript
    """)
    #end of notes


    #start of practice
async def Practice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=""" 
          Here are few websites from were you can practice 
        
    ~ https://www.geeksforgeeks.org/ - Geeks for geeks
    ~ https://www.javatpoint.com/    - JavaTpoint
    ~https://www.w3schools.com/js/   -W3schools
    ~https://leetcode.com/          -Leet code
    ~https://www.hackerrank.com/    -Hacker rank
    """)




async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
-Mail:  bonagiripraneeth07@gmail.com
-Github:https://github.com/bonagiripraneeth07
    """)

from telegram.ext import CommandHandler

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    getstarted_handler =CommandHandler('getstarted',getstarted)
    Roadmaps_handler = CommandHandler('roadmaps',roadmaps)
    help_handler = CommandHandler('help',getstarted)
    Youtube_handler =CommandHandler('Youtube',Youtube)
    contact_handler =CommandHandler('contact',contact)
    Fronted_handler=CommandHandler('Frontend',Fronted)
    Backend_handler = CommandHandler('Backend', Backend)
    DevOps_handler = CommandHandler('Devops', DevOps)
    FullStack_handler = CommandHandler('Fullstack', FullStack)
    AIandDataScientist_handler = CommandHandler('AIandDataScientist',AIandDataScientist)
    DataAnalyst_handler = CommandHandler('DataAnalyst', DataAnalyst)
    React_Roadmap_handler = CommandHandler('React_Roadmap',React_Roadmap)
    Angular_Roadmap_handler = CommandHandler('Angular_Roadmap', Angular_Road_map)
    Nodejs_Roadmap_handler = CommandHandler('Nodejs_Roadmap', Nodejs_Roadmap)
    Python_Roadmap_handler = CommandHandler('Python_Roadmap', Python_Roadmap)
    Java_Roadmap_handler = CommandHandler('Java_Roadmap', Java_Roadmap)
    DSA_Roadmap_handler = CommandHandler('DSA_Roadmap', DSA_Roadmap)
    More_handler = CommandHandler('More', More)
    Python_handler =CommandHandler('Python',Python)
    Java_handler  =CommandHandler('Java',Java)
    HTML_CSS_handler =CommandHandler('HTML_CSS',HTML_CSS)
    Javascript_handler=CommandHandler('javascript',Javascript)
    Androidstudio_handler=CommandHandler('Androidstudio',Androidstudio)
    C_handler =CommandHandler('C',C)
    PostgreSQL_handler =CommandHandler('PostgreSQL',PostgreSQL)
    Notes_handlers=CommandHandler('Notes',Notes)
    Practice_handler=CommandHandler('Practice',Practice)




    #adding handlers
    application.add_handler(start_handler)
    application.add_handler(getstarted_handler)
    application.add_handler(help_handler)
    application.add_handler(React_Roadmap_handler)
    application.add_handler(Python_Roadmap_handler)
    application.add_handler(Nodejs_Roadmap_handler)
    application.add_handler(DSA_Roadmap_handler)
    application.add_handler(Java_Roadmap_handler)
    application.add_handler(Angular_Roadmap_handler)
    application.add_handler(More_handler)
    application.add_handler(Youtube_handler)
    application.add_handler(contact_handler)
    application.add_handler(Roadmaps_handler)
    application.add_handler(Fronted_handler)
    application.add_handler(Backend_handler)
    application.add_handler(AIandDataScientist_handler)
    application.add_handler(DevOps_handler)
    application.add_handler(DataAnalyst_handler)
    application.add_handler(FullStack_handler)
    application.add_handler(Python_handler)
    application.add_handler(Java_handler)
    application.add_handler(Javascript_handler)
    application.add_handler(C_handler)
    application.add_handler(HTML_CSS_handler)
    application.add_handler(PostgreSQL_handler)
    application.add_handler(Androidstudio_handler)
    application.add_handler(Notes_handlers)
    application.add_handler(Practice_handler)


    application.run_polling()
