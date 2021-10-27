FROM openjdk:8

# EXPOSE 8000

ENV CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"

RUN apt-get update
RUN apt-get install vim -y

RUN cd /usr/local/lib && curl -O https://www.antlr.org/download/antlr-4.9-complete.jar

# RUN cd /usr/local/bin \
#     && ln -s antlr4 java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool \
#     && ln -s grun java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig

# RUN alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
# RUN alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'

WORKDIR /app

CMD ["/bin/bash"]
